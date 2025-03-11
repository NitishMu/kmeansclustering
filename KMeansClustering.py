from sklearn import datasets
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
iris=datasets.load_iris()
X=iris.data
k=3
kmeans=KMeans(n_clusters=k)
kmeans.fit(X)
centroids=kmeans.cluster_centers_
labels=kmeans.labels_
plt.figure(figsize=(8,6))
plt.scatter(X[:,0], X[:,1],c=labels,cmap='viridis')
plt.scatter(centroids[:,0],centroids[:,1],marker='x',s=200,c='red',label='Centroids')
plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title('k-means clustering of Iris Dataset')
plt.legend()
plt.show()
