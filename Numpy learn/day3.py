import numpy as np
#1.universal function ，或 ufunc ，是用来在 ndarray 中实现 element - wise 操作的。
#可以认为这个 ufunc 可以把一些简单的函数做快速的向量化封装，输入是一个以上的标量，输出也是一个以上的标量。
#很多 ufuncs 都是点对点的变换，像 sqrt 或 abs :
#一元通用函数
print(np.abs(-10))
arr=np.array([-10,-45,22,46])
print(np.abs(arr))  
print(np.sqrt(4))  #求平方根，求结果返回位小数形式

#向上取整，向下取整
arr=np.array([1.1,2.3,2.6])
print(np.ceil(arr))
print(np.floor(arr))
#四舍五入
print(np.rint(arr))

#二元通用函数

#2.统计相关函数
arr=np.arange(10,20)
print(np.sum(arr))  
#等价于   统计相关函数，可以直接用数组调用
print(arr.sum())

#针对于高维度数组，mean,sum这样的函数能接受axis作为参数来统计数值，返回结果的维度更少
arr=np.arange(10,30).reshape(4,5)
print(arr)
#二维数组可以传入0，1 三维0，1，2
print(np.sum(arr,axis=0))  #按列  
print(np.sum(arr,axis=1))  #按行
#0和1是一种方向，0表示沿每一行向下，1表示沿每一列向右


#3.排序和唯一值
arr=np.array([20,100,50,30,80])
#注意会返回一个新的数组，原始数组不会发生变化，默认是升序
print(np.sort(arr))
#降序排列，利用切片倒转
print(arr[::-1])
arr=np.array([10,10,20,30,20])
print(np.unique(arr))
#生成一个没有重复的数组，并且数组是经过排序的





