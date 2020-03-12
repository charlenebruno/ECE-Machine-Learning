import matplotlib.pyplot as plt
import numpy as np

#Getting X and Y
data = np.loadtxt(fname = "data_pca.txt")
data = np.loadtxt(fname = "data_kmeans.txt")
X1=data[:,:1]
X2=data[:,1:]

fig = plt.figure()
ax = fig.gca()

ax.scatter(X1, X2,marker="x")
ax.scatter(1, 2,marker="x")

ax.set_xlabel('X1 Label')
ax.set_ylabel('X2 Label')
plt.show()