from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataurl="https://gist.githubusercontent.com/Thanatoz-1/9e7fdfb8189f0cdf5d73a494e4a6392a/raw/aaecbd14aeaa468cd749528f291aa8a30c2ea09e/iris_dataset.csv"

irisdf = pd.read_csv(dataurl)

print(irisdf.head(3))
sns.pairplot(irisdf, hue="target")
plt.show()