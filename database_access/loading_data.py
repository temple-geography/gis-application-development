import os, csv
from sqlalchemy import create_engine, MetaData
from sqlalchemy import insert

#######################################################################
# If running immediately after creating_tables.py in the same session,
# metadata object and table objects are already available. This section
# can be skipped.
data_dir = "database_access"
url = "sqlite:///" + os.path.join(data_dir, "transactions.sqlite")

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
#######################################################################
# Skip to this line if database engine and table objects already exist.
#######################################################################

# Function accepts table object, loads data from CSV and writes to table.
# CSV must have same name as table in database, e.g. "cutomer.csv" loads to "customer" table
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

# List of table object in order appropriate for foreign key relationships
tables = [
    customer_table,
    address_table,
    product_table,
    order_table,
    item_table
]

# Load data for all tables
for table in tables:
    load_data(table)

# # Test that data is loaded
# from sqlalchemy import select
# stmt = select(customer_table)
# with engine.connect() as conn:
#     for row in conn.execute(stmt):
#         print(row)

# # Resultset
# # (1, 'Joe')
# # (2, 'Mary')
# # (3, 'Sue')

