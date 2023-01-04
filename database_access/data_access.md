# Database Access with SQL Alchemy

## About

SQLAlchemy provides a nice Pythonic way of interacting with databases. Rather than dealing with differences between specific dialects of traditional SQL, you can leverage the Pythonic framework of SQLAlchemy to streamline your workflow and more efficiently query your data. SQL Alchemy has two main components: Core and Object-Relational Mapping (ORM). Applications can use one or both. This workshop will focus on the Core.

## Connecting to a database

The Engine is the starting point for any SQLAlchemy application. An engine is a common interface to a database, and the information it requires to connect to one is contained in a connection string. In general, connection strings have the form `dialect+driver://username:password@host:port/database`.

PostgreSQL uses psycopg2 as its driver, but more examples for common connection styles can be found at <https://docs.sqlalchemy.org/en/14/core/engines.html>.

```python
from sqlalchemy import create_engine 
db = 'connection_string'
engine = create_engine(db)
#print table names
print(engine.table_names())

#establish connection to access and manipulate database
conn = engine.connect()
```

## Table Reflection

SQLAlchemy can be used to automatically load tables from a database using something called reflection. Reflection is the process of reading the database and building the metadata based on that information. There is also the option to create a Table by hand, but reflection is very useful for working with existing databases. To perform reflection, you will first need to import and initialize a MetaData object. MetaData objects contain information about tables stored in a database. During reflection, the MetaData object will be populated with information about the reflected table automatically, so we only need to initialize it before reflecting by calling MetaData(). You will also need to import the Table object. Then, you use this Table object to read your table from the engine, autoload the columns, and populate the metadata. To autoload the columns with the engine, you have to specify the keyword arguments `autoload=True` and `autoload_with=engine`. Finally, to view information about the object you just created, you will use the `repr()` function. For any Python object, `repr()` returns a text representation of that object. For SQLAlchemy Table objects, it will return the information about that table contained in the metadata.

```python
from sqlalchemy import MetaData, Table
#Initialize metadata 
metadata=MetaData()

#Reflect Table
customer = Table('customer', metadata, autoload=True, autoload_with=engine)

print(repr(customer))
print(customer.columns.keys())
```


## SQL Queries

### Selecting

When using SQLAlchemy, you will go through the Table object instead of raw SQL queries. SQLAlchemy will take care of translating your query to an appropriate SQL statement for you.  We first want to query all needed records in the specified table using the `select()` function. This function requires a list of tables or columns as arguments. We 
execute the query and store the results in a result proxy.  We can then fetch as many results as we need. Examples include `fetchall()`, `fetchmany(number_of_rows)`, `fetchone()`, etc. We can iterate over the result proxy or use indexing to print specific columns.

```python
from sqlalchemy import select 

#bulid statement to query all records in customer table using the select() function.
stmt = select([customer])

#execute the selection and store in the result proxy
results = conn.execute(stmt).fetchmany(size=10)
print(results)

stmt = select([customer])
results = conn.execute(stmt).fetchall()

first_row = results[0]
first_row['first_name']
```


### Filtering and Targeting

We can create more specific queries with a `where()` clause. Any Python comparison operator can be used inside the `where()` clause. We can also use `in_` to include records in a specified list or conjunctions such as `and_()`, `or_()`, and `not_()`. See documentation for full list of expressions


```python
from sqlalchemy import and_
film = Table('film', metadata, autoload=True, autoload_with=engine)
print(film.columns.keys())

stmt = select([film])
stmt = stmt.where(film.columns.rating=='G')
results = conn.execute(stmt).fetchmany(size=10)
for result in results:
    print(result.title, result.release_year)

stmt = select([film])
stmt = stmt.where(
    and_(film.columns.release_year == 2006, 
         film.columns.rating != "NC-17"))
results = conn.execute(stmt).fetchall()
for result in results:
    print(result.title)
```


### Grouping, Ordering, and Built-in Functions

To sort the output by a field use the .order_by method.  By default this method sorts from lowest to highest. To reverse, use the desc() function around the column.  You can also order multiple columns as each column will be fully sorted from left to right.

```python
from sqlalchemy import desc, Float, case, cast, func
stmt = select([film.columns.title, film.columns.length, film.columns.rating])
stmt = stmt.order_by(film.columns.rating, desc(film.columns.length), film.columns.title)
results = conn.execute(stmt).fetchall()
print(results)
```

SQL Alchemy's func module provides access to built in SQL functions for quickly finding averages, sums, counts, etc.  Using the .group_by method, we can organize the results as needed. We can also use the case() expression to operate on data that meets a specific criteria.  When performing calculations, the cast() function can be used to convert an expression to a certain type.

```python
#Calculate the average length of film for each rating
stmt = select([film.columns.rating, func.avg(film.columns.length)])
stmt = stmt.group_by(film.columns.rating)
results = conn.execute(stmt).fetchall()
print(results)


#What percent of the entire rental duration is R-rated films
r_length = func.sum(
    case([(film.columns.rating=='R', film.columns.rental_duration)], 
         else_ = 0))
total_dur = cast(func.sum(film.columns.rental_duration),Float)
stmt = select([r_length/total_dur*100])
percent_r = conn.execute(stmt).scalar() # Use .scalar() for getting just the value of a query that returns only one row and column.
print(percent_r)
```

## Display Results as Pandas Dataframe

```python
import pandas as pd

stmt = select([film.columns.rating, func.avg(film.columns.length).label("average length")])
stmt = stmt.group_by(film.columns.rating)

results = conn.execute(stmt).fetchall()

df = pd.DataFrame(results)
df.columns = results[0].keys()
print(df)
```

## Practice
1. Calculate the average amount per customer_id in the payment table of the database.
2. Display the result as a dataframe showing only the customer_id and average.  Label the average column as `"average_amount"`.
3. Fetch 10 records.
