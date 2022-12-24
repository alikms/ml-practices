import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

df=pd.read_csv('data\\titanic.csv')
df['male']=df['Sex']=='male'
x=df[['Pclass', 'male', 'Age', 'Siblings/Spouses',
      'Parents/Children', 'Fare']].values
y=df['Survived'].values

model=LogisticRegression()
x_train,x_test,y_train,y_test=train_test_split(x,y)
model.fit(x_train,y_train)
print(model.predict([[3,True,22.0,1,0,7.25]]))
print(model.predict(x[:5]))

print(model.coef_,'    ^^^^^^^^    ',model.intercept_)

print(df.head())
y_pred=model.predict(x_test)
print((y_test==y_pred).sum())
print('y.size:',y.size)
print(y.shape[0])       #<-- for total number use this
print((y_test==y_pred).sum()/y.shape[0])
print('model.score(x,y):',model.score(x_test,y_test))

from sklearn.metrics import accuracy_score,precision_score , recall_score,f1_score,confusion_matrix
print('accuracy_score(y_test,y_pred):',accuracy_score(y_test,y_pred))
print('precision_score(y_test,y_pred):',precision_score(y_test,y_pred))
print('recall_score(_testy,y_pred):',recall_score(y_test,y_pred))
print('f1_score(_testy,y_pred):',f1_score(y_test,y_pred))
print('reversed (negatives first)confusion_matrix(_testy,y_pred):','\n',confusion_matrix(y_test,y_pred))

