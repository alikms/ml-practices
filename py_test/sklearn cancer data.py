from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.linear_model import LogisticRegression
cancer_data=load_breast_cancer()
print(cancer_data['DESCR'])

print(dir(cancer_data))
print('%%%%%%%%%')
print(cancer_data.keys())
#print(cancer_data.data)
print(cancer_data['data'])
print(cancer_data['data'].shape)
df=pd.DataFrame(cancer_data['data'],
                columns=cancer_data['feature_names'])
df['target']=cancer_data['target']
print("*************")
print(df[:5])
print(cancer_data['target_names'])
X=df[cancer_data.feature_names].values
Y=df['target'].values
model=LogisticRegression(solver='liblinear')
model.fit(X,Y)
print(model.predict([X[0]]))
print("model score : ",model.score(X,Y))
