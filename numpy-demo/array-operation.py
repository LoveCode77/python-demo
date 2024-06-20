import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# 输出数组的形状
print(a.shape)
# 输出数组的大小（元素个数）
print(a.size)
# 输出数组的维度数
print(a.ndim)
# 访问矩阵第一行第二列的元素
print(a[0, 1])
# 切片操作，访问前两行、从第二列开始到最后一列的所有元素
print(a[0:2, 1:])
# 数组运算：
# NumPy支持数组间的元素级运算。
# 对应元素相加
b = a + a
print(b)
# 数组与常数相乘
c = a * 10
print(c)
# 计算两个矩阵的点积（矩阵乘法）
h = np.dot(a, a)
print(h)
