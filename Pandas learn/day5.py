#唯一值、值计数、会员
import pandas as pd 
s=pd.Series([10,50,20,100,80,10,50])
k=s.unique()  #会得到一个没有重复值的numpy数组
print(k)

#value_counts 值计数  （重要）计算series中重复值出现的次数
dic={'names':['张三','李四','王五','赵六','张飞','关羽'],
     'ages':[20,33,20,54,23,11],
     'gender':['男','女','男','女','男','男'],
     'height':[1.67,1.78,1.70,1.80,1.75,1.73]}
df=pd.DataFrame(dic)

#获取男性和女性人数
k=df.gender.value_counts()
print(k)
print(k['男'])


#会员
k=df[(df.names=='张三')|(df.names=='王五')]
print(k)

#isin() 是 pandas 中用于数据筛选的重要方法，它可以快速判断元素是否存在于指定集合中
k=df[df.names.isin(['张三','王五'])]
print(k)