# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:51:43 2022

@author: tug67775
"""
### Working With ORM ###

# Version Check
import sqlalchemy
sqlalchemy.__version__ 

# Create Engine, With ORM 
engine = sqlalchemy.create_engine('postgresql://postgres:postgres@localhost:5433/ormt', echo =True)

#The first time a method like Engine.execute() or Engine.connect() is called, 
#the Engine establishes a real DBAPI connection to the database, 
#which is then used to emit the SQL. When using the ORM, 
#we typically don’t use the Engine directly once created; instead, 
#it’s used behind the scenes by the ORM as we’ll see shortly.

## Create Session ##
from sqlalchemy.orm import sessionmaker 

Session = sessionmaker(bind=engine)

session = Session()

#wraps transactions in detail 



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
    works = Column(Integer)
    
# The repr defines the format of how you want your data depicted
    def __repr__(self):
       return "<User(name='%s', fullname='%s', nickname='%s', works='%s')>" % (
                            self.name, self.fullname, self.nickname, self.works)

## Creating table from meta ##
# Having defined the metadata through mapping we can now see the object by inspecting the table

Base.metadata.create_all(engine)
# This commits the tables metadata into a table to our database 

rick_smathers = User(name = 'Rick',
                     fullname = 'Rick Smathers',
                     nickname = 'Ricky',
                     works = 1)
                    

#Add new user to session 

session.add(rick_smathers)
session.commit()

# Accessing Attributes 

print(rick_smathers.id)

# Bulk Inserts 

u1 = User(name = 'Victor',
          fullname = 'Victor Hugo',
          nickname = 'Marie',
          works = 18)
u2 = User(name = 'Emile',
          fullname = 'Emile Zola',
          nickname = 'Antoine',
          works = 16)

session.bulk_save_objects([u1, u2])
session.commit()

print(u1.id)

users = session.query(User).all()
print(users)

#
for users in session.query(User):
    print(users) 

# using funcions   

print(session.query(User.nickname, User.name).first())

#labeling
from sqlalchemy import func 
# imports postgres sql functions 
works_count = session.query(func.sum(User.works)).scalar()
print(works_count)

work_count = session.query(func.count(User.fullname) \
                           .label('works_count')).first()

print(work_count.keys())    
print(work_count.works_count)
                           
                           