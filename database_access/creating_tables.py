# Data downloaded from
# https://github.com/writeson/the-well-grounded-python-developer/tree/integration/examples/CH_10/examples/02

# Object creation based on SQLAlchemy "Working with Database Metadata"
# https://docs.sqlalchemy.org/en/20/tutorial/metadata.html
# This uses SQLAlchemy Core, *not* ORM. Textbook uses ORM.

import os
from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey

data_dir = "database_access"
url = "sqlite:///" + os.path.join(data_dir, "transactions.sqlite")

engine = create_engine(url, echo=True)

metadata_obj = MetaData()

# Define tables
# All tables definitions are stored *in* the passed metadata_obj for the database
customer_table = Table(
    "customer",
    metadata_obj,
    Column("customer_id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

order_table = Table(
    "order",
    metadata_obj,
    Column("order_id", Integer, primary_key=True),
    Column("customer_id", ForeignKey("customer.customer_id"), nullable=False),
    Column("address_id", ForeignKey("address.address_id"), nullable=False)
)

address_table = Table(
    "address",
    metadata_obj,
    Column("address_id", Integer, primary_key=True),
    Column("street", String),
    Column("zipcode", String(5)) 
)
 
product_table = Table(
    "product",
    metadata_obj,
    Column("product_id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)

item_table = Table(
    "item",
    metadata_obj,
    Column("item_id", Integer, primary_key=True),
    Column("order_id", ForeignKey("order.order_id"), nullable=False),
    Column("product_id", ForeignKey("product.product_id"), nullable=False),
    Column("qty", Integer, nullable=False)
)

# Create all tables in the database pointed to by engine
# as defined in the metadata_obj
metadata_obj.create_all(engine)