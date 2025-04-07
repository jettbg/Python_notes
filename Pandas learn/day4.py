#索引，选取，过滤
import pandas as pd
#1.Series
s=pd.Series([10,30,40,50])
print(s)
s=pd.Series([10,30,40,50],index=['a','b','c','d'])
#用标签来切片时，和python不一样，左闭右也闭，意思是头尾都可取
print(s['a':'c'])
#可以给选中的标签更改值
s['a':'c']=99
print(s)

#2.DataFrame  索引
dic={'names':['张三','李四','王五','赵六','张飞','关羽'],
     'ages':[20,33,21,54,23,11],
     'gender':['男','女','男','女','男','男']}
df=pd.DataFrame(dic)
#对于DataFrame,indexing可以通过一个值或序列，选中一个以上的列
print(df['names'])  
print(df.names)
#取一个值返回的是series
#两个则是dataframe
print(df[1:3])  #直接切片，作用的是行，了解即可
#也可以通过布尔数组索引
print(df[df.ages>20])  #布尔数组的数据作用于dataframe时，针对的是行
 
#3.获取列和行 loc iloc方法
#iloc使用整数索引 loc使用标签索引
dic={'names':['张三','李四','王五','赵六','张飞','关羽'],
     'ages':[20,33,21,54,23,11],
     'gender':['男','女','男','女','男','男']}
df=pd.DataFrame(dic)
print(df.iloc[0] ) #取出了第零行
print(df.iloc[0,2])  #取出了0行2列
print(df.iloc[:3,:2])  #iloc配合切片索引
print(df.iloc[[0,2,4],:2])  #花式索引
 #loc
print(df.loc[:2,'names':'ages']) #使用标签进行索引时，会包含结束值
#这个逗号前能用数字是因为，这个dataframe中行本来就是数字0，1，2，3，若index为a,b,c,d 则不可




