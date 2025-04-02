import pandas as pd
s=pd.Series([10,30,200,100])
s=s.drop(1)
print(s)
#也可以指定多个索引删除
s=pd.Series([10,30,200,100])
s= s.drop([1,3])
print(s)

#对于DataFrame，drop方法按行或列删除数据
dic={'names':['张三','李四','王五','赵六','张飞','关羽'],
     'ages':[20,33,21,54,23,11],
     'gender':['男','女','男','女','男','男']}
df=pd.DataFrame(dic)
#drop方法用在dataframe中，默认按行删除
print(df.drop(2))
#多个索引删多行
df=df.drop([0,3,5])
print(df)

#删除列，必须指定轴（axies）
df=df.drop('gender',axis=1)  #0行，1列
print(df)
#删除性别为男的数据
#布尔类型的series也可以对DataFrame进行过滤
dic={'names':['张三','李四','王五','赵六','张飞','关羽'],
     'ages':[20,33,21,54,23,11],
     'gender':['男','女','男','女','男','男']}
df=pd.DataFrame(dic)
r= df[df['gender'] == '男']
r.index
df=df.drop(r.index)
print(df)