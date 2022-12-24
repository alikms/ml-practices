import pandas as pd
a=pd.DataFrame([[[1,2],[3,4]],[[5,6],[7,8]]])
b=pd.DataFrame([[[10,20],[30,40]],[[50,60],[70,80]]])
c=pd.concat([a,b],axis=1)
