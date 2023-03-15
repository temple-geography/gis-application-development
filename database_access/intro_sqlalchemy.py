# -*- coding: utf-8 -*-


#%%
###Connect to the database###

import sqlalchemy as sa

# db = "dialect+driver://username:password@host:port/database"
# Driver is usually not necessary
# Usually make sure not to store password in public code
# Usual defaults, e.g. port=5432

username = "psm_student"
password = "xxxxxxxx" # Insert real password here
host = "tucla-postgis.eastus.cloudapp.azure.com"
port = "5432" # This is usually 5432 for a Postgres database
database = "universe"

db = f"postgresql://{username}:{password}@{host}:{port}/{database}" # db = 'connection_string'
engine = sa.create_engine(db, future=True)

# More verbose messages:
# engine = sa.create_engine(db, echo=True, future=True)

# Use with-block to keep connection open only while in use.
with engine.connect() as conn:
    result = conn.execute(sa.text("SELECT 'hello world'"))
    print(result.all()) 

# List schemas
insp = sa.inspect(engine)
db_list = insp.get_schema_names()
print(db_list)

sql = "SELECT * FROM films.films LIMIT 100;"
with engine.connect() as conn:
    result = conn.execute(sa.text(sql))
    print(result.all()) 

# Use parameterized quries to prevent SQL injection attacks
sql = "SELECT * FROM films.films LIMIT 100;"
with engine.connect() as conn:
    result = conn.execute(sa.text(sql))
    print(result.all()) 

# Ger more info about films table
#Initialize metadata 
# metadata_obj = sa.MetaData()
films = sa.Table("films", sa.MetaData(schema = "films"), autoload=True, autoload_with=engine)

print(films.columns)
print(films.primary_key)

# Access table data in tuples:

sql = "SELECT title, release_year, country FROM films.films LIMIT 100;"
with engine.connect() as conn:
    result = conn.execute(sa.text(sql))
    for title, release_year, country in result:
        print(f"Title: {title}\nRelease Year:\n{release_year}\nCountry: {country}\n")
    

# Use parameterized queries to prevent SQL injection attacks
sql = "SELECT * FROM films.films LIMIT 100;"
with engine.connect() as conn:
    result = conn.execute(sa.text(sql))
    print(result.all()) 
