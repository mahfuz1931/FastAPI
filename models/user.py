from sqlalchemy import Table, Column, Integer, String
from config.db import meta, engine

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255))
)

# ✅ This ensures the table is created in the database
meta.create_all(engine)
