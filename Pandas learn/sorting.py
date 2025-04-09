#排序
import pandas as pd 
s=pd.Series([10,50,20,100,80])
s.sort_index #根据索引排序
k=s.sort_values() #根据值排序 默认升序
print(k)
k=s.sort_values(ascending=False)  #表示降序
print(k)

#2.DataFrame
dic={'names':['张三','李四','王五','赵六','张飞','关羽'],
     'ages':[20,33,20,54,23,11],
     'gender':['男','女','男','女','男','男'],
     'height':[1.67,1.78,1.70,1.80,1.75,1.73]}
df=pd.DataFrame(dic)

#by指定排序的字段，可以传入单列，也可以多列
k=df.sort_values(by='ages')
print(k)
k=df.sort_values(by='ages',ascending=False)
print(k)

#优先按照年龄升序排序，如果相同，则按照身高升序排列
k=df.sort_values(by=['ages','height'])
print(k)
#优先按照年龄降序排序，如果相同，则按照身高降序排列
k=df.sort_values(by=['ages','height'],ascending=False)
print(k)