import numpy as np
# 创建随机数组
random=np.random.random((2,3))
print(random)

np.random.seed(42)
random=np.random.random((5,5))
print(random)

# 数组求和
np_sum = np.sum(random)
print(np_sum)
# 数组最大值
np_max = np.max(random)
print(np_max)
# 数组平均值
mean = np.mean(random)
print(mean)
