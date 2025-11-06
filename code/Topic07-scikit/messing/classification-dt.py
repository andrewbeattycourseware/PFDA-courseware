#from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


dataurl="https://gist.githubusercontent.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a/raw/aaecbd14aeaa468cd749528f291aa8a30c2ea09e/iris_dataset.csv"

irisdf = pd.read_csv(dataurl)

print(irisdf.head(3))

colnames=["sepal length (cm)", "sepal width (cm)","petal length (cm)","petal width (cm)"]
x = irisdf[colnames]
#x = irisdf["sepal length (cm)", "sepal width (cm)"]
y = irisdf["target"]

# ok lets pick a clasifier 
#knn
#from sklearn.neighbors import KNeighborsClassifier
#estimator = KNeighborsClassifier(n_neighbors=5)

#decision tree
from sklearn.tree import DecisionTreeClassifier
estimator = DecisionTreeClassifier()

# use it
estimator.fit(x,y)
print(estimator.predict([[1.2,2.3,3.3,1.3]]))

print(estimator.score(x,y))

from sklearn import tree
import pydotplus # pip install pydotplus
# and install graphvis 
# https://graphviz.org/download/
# and include in path
import os
os.environ["PATH"] += os.pathsep + 'C:/Users/ABeatty/Desktop/Graphviz/bin/'



data = tree.export_graphviz(estimator, out_file=None, feature_names=colnames)
graph = pydotplus.graph_from_dot_data(data)
graph.write_png('mydecisiontree.png')
