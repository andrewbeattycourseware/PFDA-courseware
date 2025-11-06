import seaborn as sns
import matplotlib.pyplot as plt

# load the dataset
dataset = sns.load_dataset('tips')

# the first five entries of the dataset
#print(dataset.head())
sns.set_style('whitegrid')
#sns.scatterplot(x='total_bill',y='tip',data=dataset)
#sns.regplot(x='total_bill', y='tip', order=1, data=dataset)
sns.lmplot(x='total_bill', y='tip', order=1, data=dataset)

plt.show()
