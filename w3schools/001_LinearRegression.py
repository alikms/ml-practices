import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
x = np.array([5,7,8,7,2,17,2,9,4,11,12,9,6])
x=x.reshape(-1,1)
y = np.array([99,86,87,88,111,86,103,87,94,78,77,85,86])
y=y.reshape(-1,1)
model=LinearRegression()
model=model.fit(x,y)
x_test=np.array(np.linspace(0,20)).reshape(-1,1)
y_pred=model.predict(x_test)
plt.scatter(x,y)
plt.plot(x_test,y_pred)
plt.show()
