import numpy as np

a = np.array([2, 3, 1])
b = np.array((2, 3, 1))
x = np.array([[1, 2, 3], [3, 4, 6]])  # 2 by 3 matrix
xx = np.array([[[1, 2, 3], [3, 4, 6]], [[1, 2, 3], [3, 4, 6]]])
np.arange(1, 10, 0.1)
np.random.normal()
print(xx.ndim, x.shape, x.dtype)
np.shape(x)
np.ndim(x)
x22 = x.flatten()
x11 = x.reshape(3, 2)
np.reshape(x, (3, 2))
print(x.size, x[0], x[0, :], x[1], x[:, 1], x[0, 0], x[0, 1], x[0, 1:])
# index and slicing
x1 = np.array([[1, 2, 3], [3, 4, 6]])
x2 = np.array([[3, 2, 1], [3, 4, 6]])
o1 = np.add(x1, x2)
o2 = x1 + x2
o3 = np.power(x1, x2)
o4 = np.equal(x1, x2)
o5 = np.size(x)
o6 = np.size(x, 1)
o7 = np.size(x, 0)
o8 = np.shape(x)
o9 = np.std(x)
o10 = np.std(x, 0)
o11 = np.std(x, 1)
o12 = x.sum()
o13 = np.sum(x)
o14 = np.sum(x, 1)
z = np.random.rand(50)
y = np.random.normal(size=100)
help(np.random.normal)
r = np.array(range(1, 100), float) / 100