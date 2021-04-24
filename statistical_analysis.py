#You can follow codes via Jupyter Notebook.

import numpy as np
import seaborn as sns
iris = sns.load_dataset('iris')
np.mean(iris['petal_length']) #we get mean value
#or we can found all the columns' means
np.mean(iris.iloc[:, 0:4])

#But mean value is so sensitive for the extreme values. In thesee situations we can use median instead of mean.

np.median(iris.petal_length)

#median is equal to 50th percentile of the dataset. So we can found other percentiles via .percentile() method.

np.percentile(iris.sepal_length, 50) #we found 50th percentile. It is equal to median.
np.percentile(iris.sepal_length, 25) #we found 25th percentile.
np.percentile(iris.sepal_length, [25, 50, 75, 90]) #we found multiple percentiles.

A = [21, 19, 22, 18, 21, 19, 22, 18, 21, 19]
B = [25, 15, 29, 11, 30, 10, 26, 14, 27, 13]
#Now we have two different arrays. Their mean are both 20 but their absolute deviation are different. We can calculate like this:

A_absolute_deviation = np.absolute(A - np.mean(A))
B_absolute_deviation = np.absolute(B - np.mean(B))

print(A_absolute_deviation)
print(B_absolute_deviation)

#We can get an abstract information via found their means

np.mean(A_absolute_deviation)

np.mean(B_absolute_deviation)

#As we can see they are both same mean value but their mean absolute deviation are different.

#If we square this value, we get variance. Also we get variance using np.var() method.

np.var(A)
np.var(B)

#standard deviation is square root of var.

np.sqrt(np.var(A)) #But we can use np.std() instead of this.

np.std(A)
np.std(B)

#Variance is the absolute distance to mean, both x and y's(We take squares because of this.)
#But if we want to observe how both x and y changes together, we need value of covariance.
#In python we can find covariance via np.cov() method.

np.cov(iris.petal_length, iris.petal_width)

#Result must be positive it these values are increases or decreases together. If they have negative corelation between them, result will be negative.
#Because covariance is the product of both values' absolute distance  from mean. (1/n)*(x-x')*(y-y')
#But there is an disadvantage about covarianca. It has no unit, so there is no sense about comparing things which has different units.
#To solve this problem we divide the covarianca with product of standard deviation of two values. The result will between -1 and 1.
#p=covariance/(std.a)*(std.b)
#If the result is near to 1 that means there is a strong positive corelation. The opposite means there is strong negative corelation. This result called 'Pearson corelation'.
#If the result near to zero, that means there is weak corelation or there is not corelation.

#The python method for this value is np.corrcoef()

np.corrcoef(iris.petal_length, iris.petal_width)

#STATISTICAL GRAPHS


#A histogram is a graphical display of data using bars of different heights. In a histogram, each bar groups numbers into ranges.
#Taller bars show that more data falls in that range. A histogram displays the shape and spread of continuous sample data.
#To draw a histogram in python, we use .hist() method on matplotlib.pyplot package.
#We can define how many intervals we want via "bins=" arguement.

import matplotlib.pyplot as plt
x = [0.55, 4.22, 3.29, 3.50, 2.85, 3.16, 4.27, 8.83, 5.11, 9.62, 3.83, 5.00, 4.19, 0.43, 2.96, 4.70, 8.92, 5.35, 8.09, 5.27]

plt.hist(x, bins=10)
plt.show()
plt.hist(x, bins=5)

#Also we can add text on the graph via plt.text() method

plt.hist(x, bins=10)
plt.text(6,4, 'Histogram Graph')
plt.show()

#or we can draw with pandas
import pandas as pd

iris.plot(y='petal_length', kind= 'hist')
iris.plot.hist(y='petal_length')
iris.hist(column='petal_length')
iris.plot(y='petal_length', kind='hist')
plt.xlabel('cm')
plt.ylabel('frequency')
plt.show()

#If we want see the ratio of one value to total value we can use normed=true arg.
plt.hist(iris['petal_length'], normed=True)
plt.xlabel('cm')
plt.ylabel('frequency')
plt.show()

#Another hist graph:
iris.plot.hist(alpha=0.6)

#Also we can draw a 2d histograms with two different variables. These hist graphs also called heat maps.
