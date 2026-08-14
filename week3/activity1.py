from ucimlrepo import fetch_ucirepo 
import pandas as df
  
# fetch dataset 
iris = fetch_ucirepo(id=53) 
  
# data (as pandas dataframes) 
X = iris.data.features 
y = iris.data.targets 
  
# metadata 
print(iris.metadata) 
  
# variable information 
print(iris.variables) 
total_different_flowers = len(set(y.values.flatten()))
print(f'Total different flowers in the dataset: {total_different_flowers}')
#get total number of rows and columns in the dataset
rows, columns = X.shape 
print(f'Total number of rows in the dataset: {rows}')
print(f'Total number of columns in the dataset: {columns}')
#get the name of different flowers in the dataset
flower_names = set(y.values.flatten())
print(f'The different flowers in the dataset are: {flower_names}')
