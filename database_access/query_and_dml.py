import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy import select, insert, update, delete

# Create the database URL. For SQLite, this is a filepath.
# You may see this with the <dialect>+<driver> format:
# engine = create_engine("sqlite+pysqlite:///...", echo=True)
# The usual (but not only) driver for SQLite is pysqlite. As it is the default, we omit it.
data_dir = "database_access" # <- Change to relative or absolute path to your existing SQLite file.
url = "sqlite:///" + os.path.join(data_dir, "transactions.sqlite")

# Create the database engine
engine = create_engine(url, echo=True)

# Load database metadata
metadata_obj = MetaData()
metadata_obj.reflect(bind=engine)

# Read table definitions from the database
customer_table = metadata_obj.tables["customer"]
address_table = metadata_obj.tables["address"]
order_table = metadata_obj.tables["order"]
product_table = metadata_obj.tables["product"]
item_table = metadata_obj.tables["item"]

# Select and print all table rows
stmt = select(customer_table)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

# Query for a specific row
stmt = select(customer_table).where(customer_table.c.name == "Mary")
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

# Query using the SQL `LIKE` or `ILIKE` operator for approximate matching
stmt = select(customer_table).where(customer_table.c.name.ilike("m%"))
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

# Query using table join
stmt = select(
    order_table.c.order_id, customer_table, address_table
    ).join(customer_table).join(address_table)
with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)

# Single-row insert
stmt = insert(order_table).values(customer_id=2, address_id=2)
with engine.connect() as conn:
    result = conn.execute(stmt)
    conn.commit()

# Display newly created Order ID
print(result.inserted_primary_key)    

# Change the shipping address for the new order
new_order_id = result.inserted_primary_key[0]
stmt = update(order_table).where(order_table.c.order_id == new_order_id).values(address_id=3)
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()

# Delete (cancel) the order
stmt = delete(order_table).where(order_table.c.order_id == new_order_id)
with engine.connect() as conn:
    conn.execute(stmt)
    conn.commit()




    


