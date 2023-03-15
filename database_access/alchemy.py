# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 22:12:27 2021

@author: tum98420
"""


#%%
###Connect to the database###

from sqlalchemy import create_engine 
db = 'connection_string'
engine = create_engine(db)

#print table names
print(engine.table_names())

#establish connection to access and manipulate database
conn = engine.connect()


#%%
###Table Reflection###

from sqlalchemy import MetaData, Table
#Initialize metadata 
metadata=MetaData()

#Reflect Table
customer = Table('customer', metadata, autoload=True, autoload_with=engine)

print(repr(customer))
print(customer.columns.keys())


#%%
### Select ###
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


#%%
### Filtering and Targeting ###

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
    
    
#%%
### Grouping, Ordering, and Built-in Functions ###

from sqlalchemy import desc, Float, case, cast, func
stmt = select([film.columns.title, film.columns.length, film.columns.rating])
stmt = stmt.order_by(film.columns.rating, desc(film.columns.length), film.columns.title)
results = conn.execute(stmt).fetchall()
print(results)


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


#%%
### Display with Pandas ###

import pandas as pd
stmt = select([film.columns.rating, func.avg(film.columns.length).label("average length")])
stmt = stmt.group_by(film.columns.rating)
results = conn.execute(stmt).fetchall()
df = pd.DataFrame(results)
df.columns = results[0].keys()
print(df)


#%%
### Practice ###

#1. Calculate the average amount per customer_id in the 
#   payment table of the database.

#2. Display the result as a dataframe showing only the 
#   customer_id and average.  Label the average column 
#   as 'average amount'.

#3. Fetch 10 records.