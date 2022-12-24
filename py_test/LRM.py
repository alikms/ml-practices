import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression
df=pd.read_csv('data\\titanic.csv')
plt.scatter(df['Sex'],df['Age'],c=df['Survived'])
plt.show()
