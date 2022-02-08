# -*- coding: utf-8 -*-
"""
Created on Fri Feb  4 09:50:35 2022

@author: tug67775
"""

#%%
###Connecting to the database and creating the engine###

## The Engine is the starting point of SQL Alchemy 
## Connects a Pool and Dialect together to provide a source of database connectivity and behavior.
## Below is the format to connect to a postgres database 
import sqlalchemy as db
engine = db.create_engine('postgresql://postgres:postgres@localhost:5433/hrdep')
connection = engine.connect()
### lets use the Meta Data to make the database readable 
### take a look at the locations table 
metadata = db.MetaData()
jobs = db.Table('jobs', metadata, autoload=True, autoload_with=engine)

### We can print the column names and meta data 

print(jobs.columns.keys())


print(repr(metadata.tables['jobs']))

#%%
### Querying ###
## Below is an example on how to do a query 

##Equivalent to 'SELECT * FROM jobs'
query = db.select([jobs])

## Store select query into the result proxy
ResultProxy = connection.execute(query)

## Execute 
ResultSet = ResultProxy.fetchall()

print(ResultSet[:3])

#%%
### Filtering Data ### 
## Find all jobs that make above 5,000

query = db.select([jobs])
query = query.where(jobs.columns.min_salary >= '5000.00')
results = connection.execute(query).fetchmany(size=10)
for result in results :
    print(result.min_salary, result.job_title)
    
# Some SQL Operators
employees = db.Table('employees', metadata, autoload=True, autoload_with=engine) 
query = db.select([employees])
query = query.where(db.and_(employees.columns.salary >= '5000.00',
        employees.columns.department_id == 8))
results = connection.execute(query).fetchmany(size=10)
for result in results :
    print(result.salary, result.last_name, result.job_id)

# More SQL Operators can be read about online
#.group_by
#db.func.sum
#.distinct

#%%
### Joining Columns and Pandas Data Frame ###  

import sqlalchemy as db
import pandas as pd

engine = db.create_engine('postgresql://postgres:postgres@localhost:5433/hrdep')
connection = engine.connect()
metadata = db.MetaData()

# Tables that already have a relationship can be joined by including both in the select statement 
employees = db.Table('employees', metadata, autoload=True, autoload_with=engine)
jobs = db.Table('jobs', metadata, autoload=True, autoload_with=engine)

query = db.select([employees, jobs])
query = query.select_from(employees.join(jobs, employees.columns.job_id == jobs.columns.job_id))
results = connection.execute(query).fetchall()

# Convert to pandas data fram
df = pd.DataFrame(results)
df.columns = results[0].keys()
df.head(5)
print(df.head(5))

#%%
### Working With ORM ###

# Version Check
import sqlalchemy
sqlalchemy.__version__ 

# Create Engine, With ORM 
engine = db.create_engine('postgresql://postgres:postgres@localhost:5433/orm', echo = False)

#The first time a method like Engine.execute() or Engine.connect() is called, 
#the Engine establishes a real DBAPI connection to the database, 
#which is then used to emit the SQL. When using the ORM, 
#we typically don’t use the Engine directly once created; instead, 
#it’s used behind the scenes by the ORM as we’ll see shortly.

### Working With ORM ###
## Declare Mapping ##
# Creating the Table user and then mapping it to a Python Class which is then referred to 
# using declaritives which replace the column objects   
from sqlalchemy.orm import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s')>" % (
                            self.name, self.fullname, self.nickname)

### WOrking With ORM ###
## Creating Schema ##
# Having defined the metadata through mapping we can now see the object by inspecting the table



   
