# -*- coding: utf-8 -*-
"""
Armando Cedano
M04 Programming Assignment
This code is the answers to the 11.1, 11.2 and 16.8 of Things To Do questions.
"""

# 11.1
# zoo.py
def hours():
    print('Open 9-5 daily')

>>> import zoo
>>> zoo.hours()
Open 9-5 daily

# 11.2
>>> import zoo as menagerie
>>> menagerie.hours()
Open 9-5 daily

# 16.8
from sqlalchemy import create_engine, select, MetaData, Table, Column, String

# Connect to the SQLite database
engine = create_engine('sqlite:///books.db', echo=True)

# Reflect the existing database into a new metadata object
metadata = MetaData()
metadata.reflect(bind=engine)

# Define the table
books_table = Table('book', metadata, autoload=True, autoload_with=engine)

# Create a connection
connection = engine.connect()

# Build a select statement to select the title column
stmt = select([books_table.columns.title]).order_by(books_table.columns.title)

# Execute the statement
result = connection.execute(stmt)

# Fetch and print the results
for row in result:
    print(row.title)
