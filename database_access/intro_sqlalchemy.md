# Introduction to SQLAlchemy

## Preparation

Download the 5 CSVs in this folder.

Begin by running the code in [creating_tables.py](creating_tables.py), followed by the code in [loading_data.py](loading_data.py). 

These scripts assume that you will use SQLite, and that you will create the SQLite database in the same folder as the CSVs that you just downloaded. In the scripts, this folder is named `database_access`. If you are working in a different folder, you will have to change the value of `data_dir`. Depending on how you are running the scripts, the relative path to `database_access` may be different, in which case you will also have to change the value of `data_dir`, or add a line to set your working directory.

If you have taken [GUS 8067 Spatial Database Design](https://leehach.github.io/spatialdb/), you are already familiar with working with PostgreSQL. You may choose to create these tables in a Postgres database instead of SQLite. See "Creating the Database Connection" below for information on modifying the database connection URL.

## SQLAlchemy Core and SQLAlchemy ORM

SQLAlchemy is a Python package used for interacting with various SQL backends in a consistent and Pythonic way. SQLAlchemy has built-in support for [several major relational databases](https://docs.sqlalchemy.org/en/20/dialects/index.html#included-dialects), including PostgreSQL, MySQL/MariaDB, SQLite, Oracle, and Microsoft SQL Server. Many other data backends are included via external packages.

SQLite support is built into Python. In fact, Python has a built-in `sqlite` module which can be used to interact with SQLite without SQLAlchemy. Why use SQLAlchemy? There are subtle differences between SQL dialects, so in many cases, SQL written for one database backend may not work against a different backend. Therefore, if your Python code uses SQL statements directly, and you (or your organization) decide to migrate to a different database, you would probably have to rewrite all but the most simple SQL statements. However, if you used SQLAlchemy, you would just make sure that the API for the new database was available, and SQLAlchemy would use the new API to communicate with the database.

This is an advantage of using SQLAlchemy Core. For some developers, there is also an advantage to using SQLAlchemy ORM, the Object Relational Mapper. We previously discussed the use of classes. Classes often represent real-world entities in the same way that database tables (relations) do. An HR application might have a Person class, the same way that an HR database might have a Person table. In fact, the HR application is probably interacting with the HR database. An ORM gives us a way to create a Person class that mimics the structure of the Person table, and to create person instances that correspond to rows in the person table. When a new instance is created, and its properties (attributes) are populated, that instance can be committed, creating a new row in the person table. Similarly, an instance can be created from an existing row, and its properties can modified in order to update the table.

Using an ORM requires additional effort, and not all developers think that this effort pays off. There are also concerns about SQLAlchemy ORM performance, although this could be addressed by either more careful construction of the code that uses the ORM, or using a different ORM than SQLAlchemy. For this course, our purpose is to learn the basics of interacting with a database using Python. I have chosen SQLAlchemy because it is perhaps the most widely known SQL package for Python. If you are steeped in the object-oriented programming paradigm, ORM may come naturally to you, and you may want to skip Core, but the SQLAlchemy docs make clear that understanding ORM is built on Core, and recommend learning Core first. This workshop will stick to SQLAlchemy Core.

One other thing to clarify. You will find things on the internet that demonstrate Core by sending fully formed SQL statements to the database, and suggest both that this is Core's primary use case, and that you need to use ORM to avoid writing SQL. This is wrong, or perhaps just poorly stated. Core allows you to work with Python objects to specify what you want to do, and will build the SQL for you. In fact, as I mentioned above, the entire purpose of using a package like SQLAlchemy is to interact with the database in a database-agnostic way, and Core does that. If you are writing the SQL yourself, you have to spend time making sure that you are constructing the SQL itself in a database-agnostic way. If you use SQLAlchemy (Core *or* ORM), SQLAlchemy will build the SQL for you, and will construct it differently for different backends.

## Creating the Database Connection

If you followed the preparation instructions, you should have a very simple Product Orders database, with a few customers and customer orders. We will perform some simple queries of this database, add a new product order, and delete a cancelled order.

Before we can do that, we need to connect to the database. To do so, we will create a database "engine", which will store the instructions for connecting to the database. This section explains both how to connect to a SQLite database, which is what the scripts included with this workshop do, and how to connect to a PostgreSQL database.

In either case, we start with a database URL, which is passed to the `create_engine()` method. We will call `create_engine()` with the parameter `echo=True`. This will cause the commands we issue and database messages to be printed in the Python console. This is not necessary for these scripts to work, but we will turn it on for learning purposes. This will mimic the experience of issuing these commands in a database client.

### Creating a SQLite Engine


The basic format of the command to create a SQLite engine is:

```python
engine = create_engine("sqlite:///filepath", echo=True)
```

Notice that the URL requires 3 slashes (`///`) after the dialect name. This only applies to the file-based SQLite database format. For RDBMSes like PostrgreSQL, the URL will have the more typical 2 slashes (as in an `http://domain` web URL).

The filepath can be a relative or absolute path. When running on Windows, you can use either forward slashes (`/`) or double backslashes (`\\`) in the filepath.

Also note that you will sometimes see the URL in the `<dialect>+<driver>` format. We are using the default `pysqlite` drive and omit it, but if we were being explicit, it would look like this:

```python
engine = create_engine("sqlite+pysqlite:///filepath", echo=True)
```

In the example scripts, we import the `create_engine()` method and build the filepath using `os.path.join()`. I follow the structure of this repository, where `database_access` is a subfolder of the root folder, and assume that the root folder is the working directory. If you name your folders differently, or if Python is running in a different working directory, you will have to change the `data_dir` in this code.

```python
from sqlalchemy import create_engine

data_dir = "database_access"
url = "sqlite:///" + os.path.join(data_dir, "transactions.sqlite")

engine = create_engine(url, echo=True)
```

Note that the database engine can be created whether or not the database exists. It is only when you attempt to connect to it that an error will be raised.

### Creating a PostgreSQL Engine

The SQLite URL is pretty simple, as it just needs a filepath to the SQLite file. For database servers, like PostgreSQL or Microsoft SQL Server, you need to specify login credentials, and a database name, since the server may be managing multiple databases.

The database URL passes this information in the following format:

```python
"dialect+driver://username:password@host:port/database"
```

As with SQLite, each dialect (that is, each major database product) has a default driver. For PostgreSQL, the default driver is `psycopg2`, which was installed when you created the `gus8066` conda environment at the beginning of the semester (i.e., it is included in the environment file). **Note that unlike with SQLite, Python does not include a built in PostgreSQL driver. You *must* install `psycopg2` or some other Postgres driver in order to use SQLAlchemy with Postgres.**

If you took GUS 8066 Spatial Database Design, you will have set up a PostGIS database running in a Docker container using [these instructions](https://leehach.github.io/spatialdb/creating_a_postgis_server_in_docker). You can access that database with the following connection information:

* Host: localhost
* Port: 5433
* Database: gis
* User: docker
* Password: docker

If you have this Docker container running, you can build the URL and create the database engine with the following code. If you have access to a different PostgreSQL instance, you will have to edit the connection parameters as appropriate for your server.

```python
from sqlalchemy import create_engine

host = "localhost"
port = "5433" # This is usually 5432 for a Postgres database
database = "gis"
username = "docker"
password = "docker"

url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(url, echo=True)
```

## Basic Query and DML

All major databases support Create, Read, Update, and Delete (CRUD) operations. Read operations are usually referred to as database **query**, and create, update, and delete operations are collectively referred to as **DML**, or **Data Modification Language**.

The first thing a database user learns is usually how to query existing data, so we will start with some basic queries. Then, we will move onto DML, with an example of an `INSERT`, `UPDATE`, and `DELETE`. After completion, the database should be in the same state as when we started; that is, we will delete the sole record that we have created.

We begin by importing the SQLAlchemy methods used for CRUD operations. We saw how to create the database engine above, and that will be omitted here.

In order to create Python commands that will interact with the database, we need objects to represent the database tables and their structure. When working with any database, we need to know what tables exist and their columns. We create these objects in Python using **reflection**. We first create a metadata object, bind it to the database engine, and use that metadata object to access these table definitions.

```python
from sqlalchemy import MetaData
from sqlalchemy import select, insert, update, delete

# Load database metadata
metadata_obj = MetaData()
metadata_obj.reflect(bind=engine) # <- engine previously created

# Read table definitions from the database
customer_table = metadata_obj.tables["customer"]
address_table = metadata_obj.tables["address"]
order_table = metadata_obj.tables["order"]
product_table = metadata_obj.tables["product"]
item_table = metadata_obj.tables["item"]
```

We can now execute CRUD operations against these tables.

### SQL `SELECT`

We start with a query which returns all rows and all columns from a single table:

```python
stmt = select(customer_table)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)
```

By passing in a table object to the `select()` method, with no other parameters or modifications, we are requesting all columns and all rows for this table.

We can view the SQL that will get sent to the database as follows:

```python
print(stmt)
```

```
SELECT customer.customer_id, customer.name 
FROM customer
```

As we have created the database engine with `echo=TRUE`, the SQL statement that gets sent to the server will always be displayed in the Python console, so I will not explicitly print the statement again.

This code block demonstrates some common patterns:

* We use the generically named variable `stmt` to hold the instructions we want to send to the database. This assumes that we only intend to use the statement once, and are OK to overwrite it on the next operation. If you will be reusing the statements, you will probably want to create variables with unique names.
* The statement itself is executed in a `with` block. A `with` block is a Python structure for creating an object and making sure that it is closed when you are done using it. In this case, we don't want to hold a connection to the database open when we aren't actually issuing commands. We will essentially create a connection, issue a command, get results, and then close the connection (automatically) for each command that we want to send to the database. We could of course put multiple commands in each `with` block, but we will never accidentally hold a connection open that is not being used.
* The commands themselves are generally executed with `conn.execute(stmt)`. For commands that return results, we may collect and inspect the results.

In this case, the resultset is a collection of rows. We use standard Python to iterate the results and print each row.

When the block runs, this output is generated:

```
2025-02-14 16:35:16,822 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2025-02-14 16:35:16,822 INFO sqlalchemy.engine.Engine SELECT customer.customer_id, customer.name 
FROM customer
2025-02-14 16:35:16,822 INFO sqlalchemy.engine.Engine [generated in 0.00025s] ()
(1, 'Joe')
(2, 'Mary')
(3, 'Sue')
2025-02-14 16:35:16,822 INFO sqlalchemy.engine.Engine ROLLBACK
```

This shows the SQL statement that was sent to the database (line 2) and also the output of each row. Notice that each row is a tuple (`(1, 'Joe')`, etc.)

Notice also that the last row contains the SQL command `ROLLBACK`. By default, SQLAlchemy does not **commit** operations in a transaction unless explicitly instructed to. As the current instruction is a query (fetch these results and show them to me), this doesn't really matter, as no changes were made to the database. When we get to DML operations like `INSERT`, you must explicitly commit the transaction, or the inserted rows are discarded.

Often we want to query for specific subsets of the data. We saw in the results above that we have a customer named Mary. Let's create a query that *only* returns Mary's record. We do so using the `where()` method.

```python
stmt = select(customer_table).where(customer_table.c.name == "Mary")
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)
```

This query outputs a single row.

In the `where()` parameters, `c` is a shorthand for `columns`, and `name` is the name of the column we want to filter on. This is the equivalent of the SQL clause `WHERE name = 'Mary'`. We will always refer to columns using this syntax: `table_name.c.column_name`.

We often want to search using an approximate match. We can do this in SQLAlchemy using the `like()` or `ilike()` method. As an example, let's find all the names that contain the letter "e".

```python
stmt = select(customer_table).where(customer_table.c.name.like("%e%"))
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)
```

This query will return two customers, Joe and Sue.

If capitalization doesn't matter, we can use the `ilike()` method for case-insensitive string comparison.

```python
stmt = select(customer_table).where(customer_table.c.name.ilike("j%"))
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)
```

This will return all customers with names starting with "J" or "j".

Interestingly, this is where we see the advantages of using SQLAlchemy. Many major databases support `ILIKE`, but it is not in the SQL standard, and is not included in SQLite. If we view the SQL statement, we see that it was sent to the database as:

```
SELECT customer.customer_id, customer.name 
FROM customer 
WHERE lower(customer.name) LIKE lower(?)
```

If you run this in PostgreSQL, you would instead see the following, because Postgres supports the `ILIKE` operator:

```
SELECT customer.customer_id, customer.name 
FROM customer 
WHERE customer.name ILIKE ?
```

By the way, what's up with the question mark in the query? Didn't we compare the customer name with the string `M%`? The query is sent to the database as a parameterized query. That is the query is sent with a placeholder for the search string, and then that search string is substituted into the query. This is a common technique that is used to prevent [SQL injection](https://en.wikipedia.org/wiki/SQL_injection) attacks. SQLAlchemy handles this for you, whereas if you built the query string yourself and sent it to the database, you would have to do your own "sanitizing" of, say, form data on a website that you manage, in order to prevent SQL injection attacks.

The last common query technique we will look at is table joins to return data from more than one table. SQLAlchemy does something helpful here. If your tables have foreign keys define, you will often want to join on the foreign key. SQLAlchemy will do this for you by default. That is, when you join to a table that has a foreign key defined, SQLAlchemy will automatically join on the foreign key column without you having to explicitly specify the join column(s). (It is also possible to join on columns other than the foreing keys by explicitly specifying them, but that will not be demonstrated here.)

In the sample Transactions database, the `order` table has foreign keys to the `customer` and `address` tables. That is, you can't create an order for a customer or address that doesn't already exist in the database. We will request the customer name, street, and zipcode columns so that we can print address labels.

The join column will get repeated in the resultset for both the left and right table. We don't want these columns repeated, so we will request only the `order_id` from the `order` table, and all columns from the `customer` and `address` table.

While there are several ways to specify table joins in SQLAlchemy, I think the simplest is the `join()` method. This lets you specify the right join table only, and the left join table is determined implicitly from the tables present in the select list. It is possible to create a statement that SQLAlchemy can't figure out the join order for. In that case, other syntaxes allow you to make the join order explicit, but for simple queries, this is usually not necessary.

Note that to join to more than one table, we just use the `join()` method additional times on the additional tables.

```python
stmt = select(
    order_table.c.order_id, customer_table, address_table
    ).join(customer_table).join(address_table)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)
```

For more complex queries, refer to [Using SELECT Statements](https://docs.sqlalchemy.org/en/20/tutorial/data_select.html) in the SQLAlchemy Tutorial.

### SQL `INSERT`

In this section, we do a single row insert into the `order` table. We use the `values()` method to specify the values that get written to the columns, using the column names (without quoting) as parameter names. Since `customer_id` and `address_id` are foreign keys, we specify values (2 and 2) that exist in the `customer` and `address` tables.

```python
stmt = insert(order_table).values(customer_id=2, address_id=2)
with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()
```

After executing the statement, we use `conn.commit()` to persist the changes in the database. As we saw before, without an explicit `COMMIT`, SQLAlchemy issues a `ROLLBACK`, and your "proposed" changes are abandoned. Why would the default be to abandon the changes?

It is common to issue complex DML instructions that may insert, update, or delete from many tables. Often these changes have to happen in a specific order, and if something goes wrong earlier in the instructions, you will want to abandon all changes rather than leave the database in an inconsistent state. For example, we just inserted an order, without specifying what items are in that order. For a more realistic example, we would want to create an order (insert into the `order` table), then add items to that order (insert into the `item` table). But putting these statements in a `with` block, if something goes wrong during the process, like your application crashing, you would not be left trying to figure out what part of the instructions were successfully completed. The whole transaction would be rolled back, and *no* tables would be changed.

Note that we have assigned the result of `conn.execute(stmt)` to a variable named `result`. This is not strictly necessary. We could run `conn.execute(stmt)` and not collect the result, but in this case the result is quite useful, as it contains the newly generated `order_id`. We can use `result` to access this value with:

```python
print(result.inserted_primary_key)    
```

```
(6,)
```

Let's store this value. The result is a tuple, so we will store the first element of the tuple for use in our `UPDATE` and `DELETE` queries.

```python
new_order_id = result.inserted_primary_key[0]
```

### SQL `UPDATE` and `DELETE`

The `update()` and `delete()` methods work fairly similarly. They both take a parameter to specify which table to update or delete from. As with `select()`, they both have an optional `where()` method that allows us to specify *which row(s)* to update or delete. If this method is omitted (no filtering criteria is specified), then *all* rows of the table are updated or deleted. The `update()` method also takes a `values()` method which, as with the `insert()` method, specified what values to write to which column(s).

Let's assume that the person who just placed an order wants to update their shipping address to `address_id` 3. We will use `new_order_id` to find the just-placed order, rather than hard-coding the value.

```python
stmt = update(order_table).where(order_table.c.order_id == new_order_id).values(address_id=3)
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()
```

Most of the elements of this code should be familiar from our previous discussion.

Now let's assume the person wants to cancel their order. We will cancel it by deleting the new order.

```python
stmt = delete(order_table).where(order_table.c.order_id == new_order_id)
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()
```

The order is cancelled.

Again, this is not very realistic. In a real world transactions database, we would probably want to preserve the fact that an order was cancelled. This row would be marked as cancelled (perhaps requiring a new column), or perhaps moved to a table of cancelled orders. In this case, I just wanted to demonstrate the syntax for the `delete()` method, and leave the database at the end of the exercise in the same state it was at the beginning.

## Creating the Database and Loading Data

At the beginning, you were asked to run some scripts without any explanation so that you would have a sample database to work with. This section delves into those scripts so that  you understand table definition and loading data with a multirow insert. You can either read through the instructions, or just delete `transactions.sqlite` and practice running the code again. You should also exit and restart your Python session, or delete the database engine and metadata objects.

### Table Definition

Before designing the tables, create the database engine and metadata objects. This looks exactly like it did when we prepared for query and DML. The code is repeated here:

```python
import os
from sqlalchemy import create_engine, MetaData

data_dir = "database_access"
url = "sqlite:///" + os.path.join(data_dir, "transactions.sqlite")

engine = create_engine(url, echo=True)

metadata_obj = MetaData()
```

Note that we do not use `MetaData().reflect(bind=engine)` to reflect the tables in the database, because the database does not exist yet! We are going to define the tables "from scratch", not reflect them from the database.

Now we import some objects we need from the SQLAlchemy module to build tables, columns, and keys. We also create our `customer` table, a simple table which will demonstrate features typical of many tables.

```python
from sqlalchemy import Table, Column, Integer, String, ForeignKey

customer_table = Table(
    "customer",
    metadata_obj,
    Column("customer_id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)
```

The table is built with the `Table()` constructor. All table names and column names are specified as strings. In this case, the table name is `customer` and the column names are `customer_id` and `name`. The second parameter is the metadata object that will contain the table.

Column data types are specified using the `Integer` and `String` types imported from SQLAlchemy. Several other types are available, such as `Boolean` and `DataTime`, although not all backends support all types. For example, SQLite does not support the `DataTime` type. Additional boolean parameters indicate whether the column is a `primary_key` (False is the default) or is `nullable`, i.e., allows null (missing) values (True, or allowing null values, is the default per the SQL standard).

We often create database tables with an autoincrementing ID column as a primary key. For SQLite, *any* integer primary key column is automatically designated as the ROWID column and will automatically be assigned a unique value if one is not provided. Thus, the `customer_id` is automatically an autoincrementing column. We made use of this above when we inserted a new value in the `order` table. We did not specify and `order_id`, and a new `order_id` was created for us and returned by the database.

For PostgreSQL, the syntax for an autoincrementing identity column is:

```python
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Identity # <- note added import

customer_table = Table(
    "customer",
    metadata_obj,
    Column("customer_id", Integer, Identity(always=True), primary_key=True),
    Column("name", String, nullable=False)
)
```

Note that SQLite does not support identity columns. If you use this syntax, `Identity(...)` will just get ignored.

Now let's create an `order` table. Orders will be linked to customers, so we will use `customer_id` as a foreign key in the `order` table.

```python
order_table = Table(
    "order",
    metadata_obj,
    Column("order_id", Integer, primary_key=True),
    Column("customer_id", ForeignKey("customer.customer_id"), nullable=False),
    Column("address_id", ForeignKey("address.address_id"), nullable=False)
)
```

Most of the code exactly mimics what we already saw for the `customer` table. The only new thing is that we have added a foreign key constraint in place of the data type. The foreign key column is passed as a string in the format `table_name.column_name`. The foreign key must be a column that is unique in the referenced table, and is usually the primary key. We do not need to specify the data type (integer), because SQLAlchemy will realize that `customer.customer_id` is an integer and set the type appropriately.

Notice that the table also has a foreign key referencing the `address` table, which has not yet been defined. The script [creating_tables.py](creating_tables.py) has code to create `address`, `product`, and `item` tables.

Once all tables are defined, the final step is to create them. This is done with one line:

```python
metadata_obj.create_all(engine)
```

The metadata object holds all the table defitions. The table definitions are basically instructions for SQLAlchemy to create the DDL (Data Definition Language) SQL statements that will create the tables. The `create_all()` method tells SQLAlchemy to create the tables defined in the metadata object, in the database specified by `engine`. Tables with foreign key relationships will automatically be created in the correct order.

**Running this line will actually create `transactions.sqlite` on disk if it does not yet exist.** The location of this file is controlled by the `data_dir` variable (which you may have modified). If the file does exist, the tables will be created in the existing file.

### Table Loading with Multirow `INSERT`

We have already seen the `insert()` method in action. The `insert()` method can also be used to insert multiple rows at once.

The code to do so is in [loading_data.py](loading_data.py). The code has several parts:

1. It opens with the necessary imports.
2. The next section is commented as optional. It creates the database engine, metadata object, and reflects the tables (i.e., loads table defintions from the database). If you run this script immediately after [create_tables.py](create_tables.py) in the same Python session, these objects already exist. If you run this as a module at the command line or using VS Code's "Run Python File in Dedicated Terminal" feature, these objects don't exist, and will need to be recreated.
3. The core of the script is a function which loads the data from CSV and uses multirow `insert()` to load those rows into the tables.
4. A commented out part at the end does a simple select on the `customer` table to confirm that the data has been loaded.

Parts 1, 2, and 4 use commands and principles we have already discussed, with the addition of importing Python's `csv` module. Let's look more closely at part 3.

Part 3 starts with a function, `load_data()`.

```python
def load_data(table_obj):

    fn = os.path.join(data_dir, table_obj.name + ".csv")
    with open(fn, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        values = [row for row in reader]

    with engine.connect() as conn:
        result = conn.execute(
            insert(table_obj),
            values
        )
        conn.commit()
```

The function takes a SQLAlchemy table object as a parameter. Remember that the table object includes the table name, which does not have to match the object name, and in this case does not. Each object name is the table name followed by the suffix `_table`. The data to be loaded is read from a CSV file whose name matches the table name. So for the `customer` table we have the following:

* Table name: `customer`
* Filename: `customer.csv`
* SQLAlchemy object name: `customer_table`

I have constructed this example so that the source CSV names match the table names. If you are working with data files that don't match your desired table names, you either have to rename the CSVs or modify the function to accept a filename parameter.

The function then opens the CSV in a `with` block, and uses `csv.DictReader()` to read the contents of the file. Each row in the file becomes a dictionary, with column names (from the CSV header) as keys. The rows are iterated in a list comprehension, giving us a list of dictionaries. The contents after reading `customer.csv` looks like this:

```python
[
    {'customer_id': '1', 'name': 'Joe'},
    {'customer_id': '2', 'name': 'Mary'},
    {'customer_id': '3', 'name': 'Sue'}
]
```

We read the data into a list of dicts because the `insert()` method can accept multiple rows of data this way.

We then write that list of dicts to the target table in a `with` block. Rather than passing previously constructed SQL statement to `conn.execute()`, we pass to parameters:

* `insert(table_obj)`, which says to insert into the passed table, but does not pass any values; that is, it is not a complete insert statement
* The values to pass as a list of dicts

As usual, this is followed by a commit to persist the changes in the database.

After the function definition, we call `load_data()` once for each table. Because of foreign key constraints, the order matters. The `order` table has foreign keys referencing `customer` and `address`, so we must load data to those tables first.

The SQLAlchemy documentation has a section on [ORM Bulk INSERT Statements](https://docs.sqlalchemy.org/en/20/orm/queryguide/dml.html#orm-bulk-insert-statements). I have not demonstrated the ORM module, and want to briefly address the concept of bulk loading.

`INSERT` statements are slow. Many RDBMSes have specialized tools for bulk loading, meaning loading many rows of data in an efficient manner. SQLAlchemy provides a way to use multirow `insert()` to speed up the usually slow insert process. This may involve things like batching the rows so that an efficient number of rows is inserted in a single operation, so that you don't have to figure out what that efficient number is. If you were going to be loading millions of rows of data, I would almost always use the RDBMS tools directly, for two reasons.

* `INSERT`s, no matter how efficiently managed will almost never match the speed of specialized bulk loading tools.
* There will be a trememndous loss of efficiency in loading a CSV that large into Python in the first place. Python file I/O does let you read individual rows or batches of rows, so you could read batches and then load them into the database, but then you are substituting your judgment for the SQLAlchemy bulk insert's judgment on efficient batch sizes, and have given up much of the advantage of relying on the ORM to manage your interaction with the database.

Of course, if you don't care about the speed, and you just want to create a push-button tool for an end user to load new data, you may choose to use Python anyway, But even in this case, I would probably use Python to control a lower-level interaction with the database using the database-specific API, such as `psycopg2`, or to control database-specific command line applications like using PostgreSQL's `\copy` command via `psql`.
