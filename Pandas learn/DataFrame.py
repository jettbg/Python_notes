#DataFrame 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔值等）。 
#DataFrame 既有行索引也有列索引，它可以被看做由 Series 组成的字典（共用同一个索引）。
#DataFrame 中的数据是以一个或多个二维块存放的（而不是列表、字典或别的一维数据结构）。
import pandas as pd
import numpy as np 

#创建DataFrame  用字典，字典里的是列表
dic={'names':['张三','李四','王五','赵六','张飞','关羽'],
     'ages':[20,33,21,54,23,11],
     'gender':['男','女','男','女','男','男']}
df=pd.DataFrame(dic)
print(df)
#DataFrame和series一样，自动给数据赋index
#对于一个较大的DataFrame，用head方法会返回前5行,在数据分析里经常用，来查看表格有什么东西
df.head()  #默认是前五行
print(df.head(2))
#可以用columns参数获取所有列名，通过index参数获取所有行索引
print(df.columns)
print(df.index)
#从DataFrame里提取一列会返回series格式
print(df.ages)  #以属性提取
print(df['ages'])   #以字典形式提取
#注意：frame[column]能对应任何列名，但frame.column的情况下，列名必须是有效的python变量名才行

#提取行 要在loc属性里用属性或名字
print(df.loc[1])  #第二行
#列值也能通过赋值改变
df.ages=35   #所有值都变成35
print(df.ages)
#如果把list或array赋给column，长度必须符合DataFrame长度
df.ages=[20,20,10,30,40,24]
print(df)

#如果列不存在，赋值会创建一个新的列。
df['height']=1.7 #如果要增加新的列，不能使用点的形式，必须是[]的形式
print(df)

#del也能像删除字典关键字一样，删除列
del df['height']
print(df)

#如果column有不同类型 ，dtype会适应所有的列
print(df.ages.dtype)  #获取类型
df.ages.astype(np.float)
print(df)