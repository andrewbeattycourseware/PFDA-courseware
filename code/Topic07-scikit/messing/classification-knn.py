import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#from sklearn.datasets import load_iris
#from sklearn.model_selection import train_test_split

dataurl="https://gist.githubusercontent.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a/raw/aaecbd14aeaa468cd749528f291aa8a30c2ea09e/iris_dataset.csv"

irisdf = pd.read_csv(dataurl)

print(irisdf.head(3))


x = irisdf[["sepal length (cm)", "sepal width (cm)","petal length (cm)","petal width (cm)"]]
#x = irisdf["sepal length (cm)", "sepal width (cm)"]
y = irisdf["target"]

# ok lets pick a clasifier
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(x,y)

print(knn.predict([[1.2,2.3,3.3,1.3]]))

print(knn.score(x,y))
