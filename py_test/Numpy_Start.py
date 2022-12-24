import numpy as np
data=[15, 16, 18, 19, 22, 24, 29, 30, 34]
print(data)
print("mean : ",np.mean(data),"median : " , np.median(data),
      "standard deviation : ",np.std(data),"variance :",
      np.var(data),"75th percentile :",np.percentile(data,75))
