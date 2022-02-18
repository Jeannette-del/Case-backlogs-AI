#!/usr/bin/env python
# coding: utf-8

# # Database exploration using Python

# ## Connecting Python to SQL Server using pyodbc
#  
# open your Python Integrated Development and Learning Environment (IDLE) and fill the server name, database and table information

# Install the following packages using pip install:
#     pyodbc, pandas and tabulate

# In[ ]:


import pandas as pd
from tabulate import tabulate
import pyodbc 

connect = pyodbc.connect('Driver={SQL Server};'
                      'Server=Serve_name;'
                      'Database=database_name;'
                      'Trusted_Connection=yes;')
data = pd.read_sql_query('SELECT * FROM table_name', connect)
print(data) #you can print data
print(tabulate(data, headers = 'keys', tablefmt = 'fancy_grid'))#print data in tabular form

