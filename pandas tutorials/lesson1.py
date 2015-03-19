# Import all libraries needed for the tutorial

# General syntax to import specific functions in a library:
##from (library) import (specific library function)
from pandas import DataFrame, read_csv

# General syntax to import a library but no functions:
##import (library) as (give the library a nickname/alias)
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number

# Enable inline plotting
%matplotlib inline

print 'Python version ' + sys.versions
print 'Pandas version ' + pd.__version__

### Create Data ###
# The initial set of baby names and birth rates
names = ['Bob', 'Jessica', 'Mary', 'John', 'Mel']
births = [968, 155, 77, 578, 973]

BabyDataSet = zip(names, births)

# create Data Frame
df = pd.DataFrame(data=BabyDataSet, columns=['Names', 'Births'])

df.to_csv('births1880.csv', index=False, header=False)

### Get Data ###
Location = r'/Users/AprilSong/Desktop/ga_ds/pandas\ tutorials/births1880.csv'
df = pd.read_csv(Location, header=None)
# df = pd.read_csv(Location, names=['Names', 'Births']) for header names


### Prepare Data ###
# Check data type of the columns
df.dtypes
# This will return:
# Names pbect
# Births int64
# dtype: object

# Check data type of Births column
df.Births.dtype
# This will return: dtype('int64')

### Analyze Data ###

# Find most popular name or baby name with highest birth rate
# Method 1: Sort dataframe and select top row
Sorted = df.sort(['Births'], ascending=False)
Sorted.head(1)
# return
  # Names  Births
# 4   Mel     973
# Method 2: Use max() attribute to find the max value

df['Births'].max()
# returns 973

# Explain the pieces:
# df['Names'] - This is the entire list of baby names, the entire Names column
# df['Births'] - This is the entire list of Births in the year 1880, the entire Births column
# df['Births'].max() - This is the maximum value found in the Births column

# [df['Births'] == df['Births'].max()] IS EQUAL TO [Find all of the records in the Births column where it is equal to 973]
# This will return:
# [0    False
# 1    False
# 2    False
# 3    False
# 4     True
# Name: Births, dtype: bool]

# df['Names'][df['Births'] == df['Births'].max()] IS EQUAL TO [Select all of the records in the Names column] WHERE [The Births column is equal to 973]

# Creating graphs
df['Births'].plot()

# Maximum value in the data set
MaxValue = df['Births'].max()

# Name associated with the maximum value
MaxName = df['Names'][df['Births'] == df['Births'].max()].values

# Text to display on graph
Text = str(MaxValue) + " - " + MaxName

# Add text to graph
plt.annotate(Text, xy=(1, MaxValue), xytext=(8,0), xycoords=('axes fraction', 'data'), textcoords='offset points')

print "The most popular name"
df[df['Births']== df['Births'].max()]









