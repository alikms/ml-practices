import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df=pd.read_csv('data/titanic.csv')
plt.scatter(df['Age'],df['Fare'],c=df['Survived'])
#c -->color yellow-->survived
plt.show()
plt.close()
