import pandas as pd
import numpy as np

# creating series and data frame

""" Series """
Labels = ["label1", "label2", "label3"]
lis_2 = [5,3,6]
ar4 = np.array([5,3,6])

#Creating a serie from a list
pd.Series(lis_2, index = [Labels])

# Data frame

list_columns = ["col1", "col2", " col3"]
List_rows = ["row1","row2","row3"]

ar5 = np.array ([[2,5,6],
                 [6,0,4],
                 [5,2,1]])

pd.DataFrame(ar5)

# Specify row/column

pd.DataFrame(ar5, index = List_rows, columns= list_columns)

# Cleaning and selection in the data

# Import of csv
data = pd.read_csv("C:/Users/Naa Odey Solomon/Downloads/banknote.csv")
data

# Ordering a Data set
order= data.sort_index(ascending=True)
order

import matplotlib.pyplot as plt
import numpy as np

# Data Simulatiom
arr = np.random.randint(0,15,size =(15,))

# Square of arr
square = arr**2

# Multiplication of arr by 4
mul = arr*4

print(arr)
print(square)
print(mul)

# Plot the Data
plt.plot(arr)
plt.plot(square)
plt.plot(mul)


# Change the xlabel
plt.xlabel("Random integers")

# Change the ylabel
plt.ylabel("Values")

# Put a legend
plt.legend(["arr","square","mul"])

# Show the Chart
plt.show()



# Scatter

plt.scatter(arr,mul)
plt.scatter(arr,square)

# Change the xlabel
plt.xlabel("Random integers")

# Change the ylabel
plt.ylabel("Values")

# Put a legend
plt.legend(["Square","Exponetial"])

# Show the Chart
plt.show()

# Tools

# Adjusting the line
plt.figure(figsize = (15,8))

# Plot the line
plt.plot(arr,alpha=0.6,color = "orange")

# Plot the line
plt.plot(square,"-o",linewidth =3)

# Plot the line
plt.plot(mul,"o")

# Change the xlabel
plt.xlabel("Random integers")

# Change the ylabel
plt.ylabel("Values")

# Title
plt.title("Graph")

# Put a legend
plt.legend(["arr","square","mul"])

# Show the graph
plt.show()

