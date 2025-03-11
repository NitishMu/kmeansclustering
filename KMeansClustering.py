from sklearn import datasets
from sklearn.cluster import k means
import matplotlib.pyplot as plt
#
iris=datasets.load_iris()
x=iris.data
#
k=3
#
k means=k means(n_clusters=k)
#
k means.fit(x)
#
centroids=k means.cluster_centers_
#
labels=k means.labels_
#
plt.figure(figsize=(8,6))
plt.scatter[x[:,0]:,1],c=labels,cmap='viridis')
plt.scatter[centroids:,0],centroids[:,1],marker='x',s=200,c='red',label='Centroids')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('k-means clustering of Iris Dataset')
plt.legend()
plt.show()
