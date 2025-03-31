import numpy as np
#1.基本索引和切片
k=[10,20,30,40]
print(k[1:3])
n=k[1:3]
n[0]=100
print(n)
print(k)
#列表的切片是产生一个新的列表，原列表并不发生改变
arr=np.array([20,100,50,60])
print(arr[1:3])
arr[1:3]=20
print(arr)
#对数组进行切片修改，是直接改变原始数组
 
#一维的切片如上
#二维切片索引
arr=np.arange(10,20)
print(arr.reshape(2,5))
#reshape方法可以更改数组的形状，但不会改变原始数组，只会生成新的数组
arr=np.arange(10,30).reshape(4,5)
print(arr)
print(arr[1:3])
print(arr[1][1]) #等价于
print(arr[1,1])  
#逗号两侧，也可以是切片，此时逗号前代表行，后代表列
print(arr[1:3,2:4])  #可以获取二维数组里的某一部分元素

#还可以整数和切片混合使用，能做低维切片
print(arr[1,:2])
#[15 16]  一维
print(arr[1:2,:2])
#[[15 16]]  二维


#2.布尔索引  过滤操作
arr=np.array([23,45,11,56,78])

print(arr[~(arr>=60)])

#花式索引   不连续索引 通过整数数组或列表来索引
arr=np.array([13,23,45,22,11])
print(arr[[1,2,4]])
print(arr[[-1,-3]])  #-1倒数第一个 -3倒数第三个
arr=np.arange(10,30).reshape(4,5)
arr=[[0,1,2],[1,2,3]]  #(0,1) (1,2) (2,3)
#花式索引和切片组合
arr=np.arange(10,30).reshape(4,5)
print(arr[[0,3],:2])



