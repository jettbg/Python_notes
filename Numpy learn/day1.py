#1.ndarray 多维数组对象
import numpy as np
k=list(range(10))
print(k)

#创建n维数组
arr1=np.array([12,32,442,11])
print(arr1)

#嵌套序列能够转换为多维数组
k=[[12,32,11],[44,34,65]]
print(k)
arr2=np.array(k)
print(arr2)

#用ndim和shape来获取数组的维度和形状
print(arr1.ndim)
print(arr2.ndim)
print(arr1.shape)
print(arr2.shape)

#np.array会自动给数据搭配适合的类型
k=np.array([10,10.6,99.99])
print(k)
k=np.array([10,10.6,99.99,'dxy'])
print(k)

#除np.numpy可创建数组之外，zeros和ones函数也可以，了解即可
print(np.zeros(5))
print(np.zeros((2,3)))
#ones生成的全是1

#arange是一个数组版的python range函数
print(np.arange(10))
print(np.arange(1,5))
print(np.arange(1,10,2))


#2.数据类型
#dtype保存数据的类型  在创建数组是转换类型
print(np.array([11,22,43,23],dtype=float))  #这里的float还可以改写为np.float64
print(np.array([11,22,43,23],dtype=str)) 
print(np.array([11.2,22.3,43.2,23.3],dtype=int)) 

#如果数组已经创建好了，可以用astype转换类型
arr=np.arange(10,20)
print(arr)
print(arr.astype(float))
#astype是返回一个新的数组，原始的数组不会发生变化

#ndarray数组计算 
#数组之所以重要，因为不用for循环就能表达很多操作，这种叫做向量化
#任何两个大小相等的数组之间的运算都是点对点
arr1=np.arange(1,5)
arr2=np.arange(6,10)
print(arr1+arr2)  #或- *  / **幂运算

#这种算数操作如果涉及标量，会涉及数组的每一个元素
print(arr1-10)

#两个数组的比较会产生布尔数组
print(arr1>arr2)
#数组和标量也可以做比较
print(arr2>6)








