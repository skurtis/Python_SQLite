#!/usr/bin/env python3
import matplotlib; matplotlib.use('pdf')
import matplotlib.pyplot as plt
import re
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy import Integer, String
from sqlalchemy import select, desc

engine = create_engine('sqlite:///world.sqlite')
# Establish engine from SQLite file of world population data
conn = engine.connect()

DBInfo=MetaData(engine)
# Extract database info
city=Table('city', DBInfo, autoload=True)
# Extract city population information

query=select([city.c.Population]).order_by(desc(city.c.Population)).limit(100)
# Select the 100 largest cities
numseq = []
num1 = []
# Set up numeric vectors
result = conn.execute(query)
# Execute the query
num2 = 1
for i in result:
     numseq = numseq + [int(re.findall('[0-9]+',str(i))[0])]
     # Select numeric population data from query
     num1 = num1 + [num2]
     num2 = num2 + 1
     # Update vectors, including one ranging from 1 to 100

fig = plt.figure()
# Establish figure

plt.plot(num1, numseq)
# Plot data on figure

fig.savefig("largest_populations.pdf")
# Save figure as a PDF file
