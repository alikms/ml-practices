from sklearn import datasets
from sklearn.linear_model import LogisticRegression
df=datasets.load_iris()
x=df['data']
y=df['target']
logit=LogisticRegression(max_iter=1000)
C = [0.25, 0.5, 0.75, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75]
scores=[]
for c in C:
   a=[c]
   logit.set_params(C=c)
   logit.fit(x,y)
   a.append(logit.score(x,y))
   scores.append(a)
print(scores)
