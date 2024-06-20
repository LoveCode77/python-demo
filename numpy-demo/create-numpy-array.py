import numpy as np

# 创建一个一维数组
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
# 创建一个二维数组（矩阵）
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(b)
# 还可以使用 numpy 提供的函数创建特定类型的数组
# 创建一个 3x3 的全零数组
c = np.zeros((3, 3))
print(c)
d = np.zeros((10, 10))
print(d)
# 创建一个 2x2 的全一数组
f = np.ones((3, 3))
print(f)
f1 = np.ones((10, 10))
print(f1)
# 创建一个 3x3 的单位矩阵（对角线上为 1，其余为 0）
g=np.eye(3)
print(g)
g1=np.eye(9)
print(g1)
