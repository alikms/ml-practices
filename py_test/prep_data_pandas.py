import pandas as pd
df=pd.read_csv('data\\titanic.csv')
df['male']=df['Sex']=='male'
X=df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
y=df['Survived']
print(X)
print('qqqqqqqqqqqqqqqqqqq')
print(y)
