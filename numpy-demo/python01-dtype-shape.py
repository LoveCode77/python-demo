# 1.数据类型（dtype）#类似python中的数据类型，可进行选择，例如：bool;int;float;complex；
#   complex 是一种内置的数据类型,用于表示复数。复数由实部和虚部组成
# 2.数组形状（shape）#用来描述数组中的数据为几行几列。
import numpy as np
a=np.array(range(10),dtype=int) #dtype可以指定数据类型，如float#
print(a)
print(a.shape)   #输出数据形状
print(a.dtype)
b=a.reshape((2,5))  #改变a的数据形状为2行5列
print(b)
print(b.shape)
print(b.dtype)   #输出a中的数据类型
print(type(a))