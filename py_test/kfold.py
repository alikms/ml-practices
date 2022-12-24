import pandas as pd
from sklearn.model_selection import KFold
from sklearn.linear_model import LogisticRegression
import numpy as np
df=pd.read_csv('data/titanic.csv')
df['male']=df['Sex']=='male'
x=df[['Age','Fare','male','Pclass','Parents/Children','Siblings/Spouses']].values
y=df['Survived'].values
kf=KFold(n_splits=5,shuffle=True)
#for train,test in kf.split(x):
#   print(train,test)
splits=list(kf.split(x))
scores=[]
for train_indices,test_indices in splits:
   x_train=x[train_indices]
   x_test=x[test_indices]
   y_train=y[train_indices]
   y_test=y[test_indices]
#print('x',x_train,x_test,'y',y_train,y_test)
#print('\n',splits)
   model=LogisticRegression()
   model.fit(x_train,y_train)
   scores.append(model.score(x_test,y_test))
print(scores)
print(np.mean(scores))
model.fit(x,y)
