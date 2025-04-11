import pandas as pd
import numpy as np

k=pd.read_csv('D:/vscode代码\联培项目\data/600519.csv')
print(k)

#查看前十行
print(k.iloc[:10])   
print(k.head(10))  #head()方法默认查看前五行

#数据集中有多少列
#获取形状得到的是元组 (298, 6) 这里提取第二个元素即为列数 
print(k.shape[1])

#打印出全部列名、
print(k.columns)

#打印数据集的索引(行名)
print(k.index)
 
#在Open这一列有多少种不同的数据(去重)
a=k['Open'].unique()
print(a)

#查看Open这一列每一种数据出现多少次
a=k['Open'].value_counts
print(a)

