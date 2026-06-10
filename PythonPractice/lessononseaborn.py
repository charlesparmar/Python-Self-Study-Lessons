import seaborn as sns
import matplotlib.pyplot as plt
df = sns.load_dataset('iris')   # load the tips dataset
print(df.head())   # print the first 5 rows of the dataset

sns.scatterplot(x = 'sepal_length', y = 'sepal_width', data = df)   # plot a scatter plot of the total bill and the tip
plt.show()   # show the plot

sns.pairplot(df, hue = 'species', size = 2)   # plot a pair plot of the dataset
plt.show()   # show the plot