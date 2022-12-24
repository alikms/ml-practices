import pandas as pd
df=pd.read_csv('data\\titanic.csv')
print(df.head(1))
print(df.describe())
col = df['Age']
print('age \n')
print(col)
print(111111111111111111111)
df2=pd.read_csv('http://sololearn.com/uploads/files/titanic.csv')
col=df2['Fare']
print('fare \n')
print(col)
col=df[['Age','Sex','Survived']]
print(col)
print(22222222222222222222)
df['male']=df['Sex']=='male'
print(df.head())
print(33333333333333333333)
print(df['Age'].values)
