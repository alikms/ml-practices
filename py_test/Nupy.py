import numpy as np
import pandas as pd
fd=pd.read_csv('data\\titanic.csv')
# ^ same as > fd=pd.read_csv('D:\\py_test\\data\\titanic.csv')
array=fd.values
col_test=array[:,2]
print(fd.head())
print(array)
print(col_test)
