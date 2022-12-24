from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
x = [4, 5, 10, 4, 3, 11, 14 , 6, 10, 12]
y = [21, 19, 24, 17, 16, 25, 24, 22, 21, 21]
data=list(zip(x,y))
inertias=[]
for i in range(1,11):
   a=[i]
   model=KMeans(n_clusters=i)
   model.fit(data)
   inertias.append(model.inertia_)
plt.plot(range(1,11),inertias,marker='o')
plt.show()
#-->n_clusters==2
kmeans=KMeans(n_clusters=2)
kmeans.fit(data)
plt.scatter(x,y,c=kmeans.labels_)
plt.show()
