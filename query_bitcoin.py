# From here on, I'll be using Python to manipulate the data extracted from the StackOverflow data dump database.

# Load pandas library and view first 6 rows of the data frame
import pandas
df = pandas.read_csv('QueryResults.csv')
print(df.head(6))

# Check duplicate ID entries, note all duplicates
df.duplicated(subset = "Id", keep = False) 
# None found! Proceeding...

# Load useful modules
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from pandas import Series

# First, view data types in the data frame
print(df.dtypes)
# CreationDate    object
# Tags            object
# Id               int64
print(type(df['CreationDate'][0]))
# <class 'str'>

# Add a dummy column of 1s to represent a mention of bitcoin for each date
df['Dummy'] = 1
print(df.head())
# Remove useless columns
df = df.drop('Unnamed: 0', 1) # 1 is the index, indicating columns
df = df.drop('Unnamed: 0.1', 1)
df = df.drop('Unnamed: 0.1.1', 1)
df = df.drop('Id', 1)
df = df.drop('Tags', 1)

print(df.head())

# Great. Write the file to save the change:
df.to_csv('simple.csv')

# Load the dataset as a pandas series
series = Series.from_csv('simple.csv', header = 0)
# Did everything load properly?
print(series.head())
'''
series.plot()
plt.show()


# Before I convert the string, I need to separate date and time
df = pandas.DataFrame(df.CreationDate.str.split(' ', 1).tolist(),
    columns = ['Date', 'Time'])
print(df.head())
# Write file to new csv
df.to_csv('dates.csv')

# Now I'll convert "Date" to a datetime object
df_dt = pandas.read_csv('dates.csv', 
    parse_dates = ['Date'], 
    index_col = ['Date'])

# Look at those dates
print(df_dt.index)

# View the file head again
print(df_dt.head())
'''


