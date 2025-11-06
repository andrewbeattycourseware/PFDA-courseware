import pandas as pd

dataurl="https://gist.githubusercontent.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a/raw/aaecbd14aeaa468cd749528f291aa8a30c2ea09e/iris_dataset.csv"

irisdf = pd.read_csv(dataurl)
print(irisdf.head(3))

colnames=["sepal length (cm)","sepal width (cm)","petal length (cm)","petal width (cm)"]
x = irisdf[colnames]
y = irisdf["target"]

# decision tree
#from sklearn import tree
#clf = tree.DecisionTreeClassifier()
# kn 
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier()

clf = clf.fit(x, y)
print(clf.predict([[1,3,4,5]]))
print(clf.score(x,y))

