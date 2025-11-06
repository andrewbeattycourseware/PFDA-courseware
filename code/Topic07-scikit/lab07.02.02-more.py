# extra
# showing samples of using seaborn to show regression plots
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# load the dataset
dataset = sns.load_dataset('tips')

# the first five entries of the dataset
#print(dataset.head())
sns.set_style('whitegrid')

#discrete input data- no jitter
#sns.lmplot(x="size", y="tip", data=dataset)
#discrete iniput data- with jitter
#sns.lmplot(x="size", y="tip", data=dataset, x_jitter=.05)
# use estimatator for the scatter plot. np.mean is the function that is used
# ie that is the function that is called for each of the result values for each discrete input
# note ths isi the range is the 95% confidence interval of the mean for the results for
# that discrete input
sns.lmplot(x="size", y="tip", data=dataset, x_estimator=np.mean)

plt.show()
