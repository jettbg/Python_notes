import pandas as pd 
import numpy as np
#numpy中用NaN表示缺失值，pandas中使用NA表示，python中用None表示
k=np.nan+10
print(k)
s=pd.Series([10,20,30,40,np.nan,50,None,pd.NA])
print(s)
#缺失值必须用函数判断，不能用==判断
print(s.mean()) #用函数会自动忽略空值，所以可以运算，自己运算则返回空值
#可以通过isnull函数将缺失值筛选出来
a=s.isnull()
print(a)

#过滤缺失数据 用dropna或notnull函数
a=s[s.notnull()]
print(a)
a=s.dropna()
print(a)


df=pd.DataFrame([[np.nan,20,30,np.nan],[20,30,np.nan,np.nan],[np.nan,np.nan,np.nan,np.nan]])
print(df)
#对于DataFrame dropna会默认删除含有缺失值的行
a=df.dropna()
print(a) 
#通过'how=all'只删除全是NA的行
a=df.dropna(how='all')
print(a)
#通过设置axis=1来删除列
a=df.dropna(axis=1,how='all')
print(a)

#填充缺失值 使用fillna来填充缺失值
s=pd.Series([10,20,30,40,np.nan,50,None,pd.NA])
a=s.fillna(20) #指定具体值填充
print(a)
a=df.fillna(1)
print(a)