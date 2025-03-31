#pandas 是 Python 数据分析的首选库。它含有使数据清洗和分析工作变得更快更简单的数据结构和操作工具。 
#pandas 经常和其它工具一同使用，如数值计算工具NumPy 和 SciPy ，分析库 statsmodels 和 scikit - learn ，和数据可视化库 matplotlib 。 
#pandas 是基于 NumPy 数组构建的，特别是基于数组的函数和不使用 for 循环的数据处理。
import pandas as pd
import numpy as np

#pandas的数据结构 Series和DataFrame
#Series 是一种类似于一维数组的对象，它由一组数据（各种 NumPy 数据类型）以及一组与之相关的数据标签（即索引）组成。
# 仅由一组数据即可产生最简单的 Series  
#1.series的使用
s=pd.Series([10,20,100,30])
print(s)
#左边表示index，右边表示对应的value。
#可通过values和index进行属性查看
print(s.index)
print(s.values) #输出的值就是Numpy的数组
#之前学的Numpy知识可以直接应用到series中  + * 比较 sqrt sum 等
print(s[0])
#print(s[-1])会报错，必须用显示出来的索引
print(s[s>20])  #布尔索引
print(s[[0,3]])   #花式索引

#创建Series时，可以指定index的标签
s=pd.Series([100,20,30,50],index=['a','b','c','d'])
print(s)
#加了自定义标签，除了可以使用标签名获取，也可以用数字索引
#使用numpy函数或类似操作时，会保留index-value的关系

#Series会自动按index排序
s1=pd.Series([10,20,100,30],index=['a','b','c','d'])
s2=pd.Series([10,20,100,30],index=['d','a','b','c'])
print(s1+s2)
#两个Series做运算时，会按照索引对齐，相加 即a和a,b和b

s1=pd.Series([10,20,100,30],index=['a','b','c','d'])
s2=pd.Series([10,20,100,30],index=['d','a','f','c'])
r=s1+s2
print(r) #series运算中，如果索引不相同，会产生空值（NaN)
print(r[1]+r[0])  #空值在参与运算时，结果也是空值
print(np.sum(r)) #系统的sum mean 会自动排除空值

#series的index能被直接更改(通过列表和数组)
s=pd.Series([100,20,30,50],index=['a','b','c','d'])
s.index=[1,2,3,4]  #通过列表改变
print(s)
s.index=np.array([10,20,30,40])  #通过numpy数组改变
print(s)
