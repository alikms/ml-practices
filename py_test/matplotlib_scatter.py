import matplotlib.pyplot as plt
import pandas as pd
df=pd.read_csv('data\\titanic.csv')
print(df['Age'])
plt.scatter(df['Age'],df['Fare'],c=df['Pclass'])
#plt.plot([x1,x2],[y1,y2])
plt.plot([0,80],[85,5])
plt.show()
plt.close()
#a=input()  print(a)->a    a Enter-> 'a'
