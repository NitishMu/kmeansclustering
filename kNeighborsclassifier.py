from sklearn import datasets
from sklearn_model_selection import train_test_split
#
iris=datasets.load_iris()
x=iris.data
y=iris.target
#
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
from sklearn.neighbors import kNeighborsclassifier
#
knn=kNeighborsclassifier (n_neighbors=3)
#
knn.fit(x_train,y_train)
#
y_pred=knn.predict(x_test)
from sklearn.metrics import accuracy_score
#
accuracy=accuracy_score(y_test,y_pred)
print(f"Accuracy:{accuray}")
