# -*- coding: utf-8 -*-
"""
Created on Fri Jan  7 20:24:15 2022

@author: Naa Odey Solomon
"""

import numpy as np
import pandas as pd

# Series

my_list = [1,2,3,4]

pd.Series(data=my_list)

# Renaming the indeces

new_indeces = ['a','b','c','d']
my_series = pd.Series(data = my_list,index=new_indeces)
my_series

my_series['c']


# DataFrames
from numpy.random import randint
df = pd.DataFrame(randint(0,100,[8,4]),['A','B','C','D','E','F','G','H'],['I','J','K','L'])
df

df.info()

# Descriptve Statistics or Summary of Data

df.describe()

# Accessing a particular column

df['J']

# Accessing a particular row
df.loc['E']

# Accessing a particular row using an integer

df.iloc[4]

# This returns a Boolean (true/false)

df['K'] >= 56

# Instead of Boolean, this returns the rows that is geater or equal to 56

df[df['K'] >= 56]


# Adding a new column to the dataframe

df.insert(4, 'M', [21,52,67,81,45,20,19,72])
df

# Deleting a column in a dataframe

del df['M']
df


##################DataFrame MEthods################################################


# The .apply() method allow you to apply a function an axis of a Dataframe
# In this example, I will add up the columns of my dataframe

def col_sum(data):
    return data.sum()

data = df.apply(col_sum)
data
########## OR
data = df.apply(lambda data: data.sum())
data


# Summing up the rows
def row_sum(data):
    return data.sum()

data1 = df.apply(row_sum, axix=1)
data1
################ OR
data1 = df.apply(lambda data: data.sum(),axis=1)
data1


####################### NULL VALUES###############################################

# The Dataframe below has a Null Value

data2 = {"Hat":[1,2,3,4],"Turtle":[5,6,np.nan,8],"Ponies":[9,10,11,12]}
df2 = pd.DataFrame(data=data2)
df2


# Dealing with a null value, either drop it or fill it in

# Dropping
df2.dropna()

# Filling
df2.fillna(3)

######### OR
df2.fillna(df2["Turtle"].mean())


############################## SEABORN #########################################
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
tips = pd.read_csv("https://media.geeksforgeeks.org/wp-content/uploads/tips.csv")
tips



sns.distplot(tips['total_bill'])
sns.displot(tips)

sns.scatterplot(data = tips, x= 'tip', y ='total_bill')

sns.pairplot(tips)

sns.kdeplot(data=tips, x='total_bill')
sns.rugplot(data=tips, x='total_bill')

sns.countplot(x='size', data=tips)

sns.stripplot(x="size", y = 'total_bill', data= tips)

tips.corr()

sns.heatmap(tips.corr())

x = sns.PairGrid(tips)
x.map(sns.scatterplot)
plt.show()