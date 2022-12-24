import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#dataframe=df
df=pd.read_csv("data/titanic.csv")#or -->
#df=pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
i=-1
for item in df.columns:
   i+=1
pd.options.display.max_columns=i
print(df.head(10))
print(df.describe())


small_df=df[['Age','Sex','Survived']]
farecol=df['Fare']
print(farecol)
#pandas dataframe to numpy array
fare_numpy_array=df['Fare'].values
print(fare_numpy_array)
#values[:10] -->first ten rows
small_numpy_array=df[['Age','Sex','Survived']].values[:10]
#small_numpy_array=df[['Age','Sex','Survived']].values[:10,:3]
print(df[['Age','Sex','Survived']].values)
#size of numpy array
print("**********")
print(small_numpy_array.shape,df.shape)
#masking
ChildMask=small_numpy_array[:,0]<18
print(small_numpy_array)
print("hhhh")
print(ChildMask.sum())
print(small_numpy_array[ChildMask])
print(small_numpy_array[small_numpy_array[:,0]<18])
#ploting basics
#import matplotlib.pyplot
#c -->color 
plt.scatter(df['Age'],df['Fare'],c=df['Survived'])
plt.xlabel("Age")
plt.ylabel("Fare")
#plt.plot -->draws a line from (0,85) to {85,5)
plt.plot([0,80],[85,5])
plt.show()
plt.close()
