from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import pandas as pd
df=pd.read_csv('cars2.csv')
X=df[['Volume','Weight']]
y=df['CO2']
scaler=StandardScaler()
X=scaler.fit_transform(X)
model=LinearRegression()
model.fit(X,y)
print(model.coef_)
