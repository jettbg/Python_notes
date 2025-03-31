#访问列表
rhyme=[1,2,3,4,5,'上山打老虎']
for each in rhyme:
    print(each,end='')
print(rhyme[0])
print('rhyme[0]')
length=len(rhyme)
print(rhyme[length-1])
print(rhyme[-1])   #列表内最后一个
print(rhyme[-2])   #列表内倒数第二个
print()
print(rhyme[0:3])
print(rhyme[:3])
print(rhyme[3:])
print(rhyme[:])
print(rhyme[0:5:2])  #第二个：后代表跨度值，从第一个数据到最后一个，故0 5 可省略
print(rhyme[::2])
print(rhyme[::-2])    #倒着来
print(rhyme[::-1])    #倒序输出整个列表

#列表的增
heros=['钢铁侠','绿巨人']
#append()  每次只能添加一个对象
heros.append('黑寡妇')
print(heros)
#extend()添加的参数必须是可迭代对象，新的内容追加到列表最后一个元素后面
heros.extend(['灭霸','鹰眼'])
print(heros)
print()
print()
print()
print()
#切片
s=[1,2,3,4,5]
s[len(s):]=[6]
print(s)
s[len(s):]=[7,8,9]
print(s)
#insert
s=[1,2,3,4]
s.insert(1,2)    #(插入位置，插入元素)
print(s)
s.insert(0,0)
print(s)
s.insert(len(s),6)
print(s)

#删
heros=['钢铁侠', '绿巨人', '黑寡妇', '灭霸', '鹰眼']
heros.remove('钢铁侠')    #remove删除指定元素
print(heros)            # 如果列表中有多个匹配元素，它会删除下标小的
                        #如果列表内不存在指定元素，就会报错
heros.pop(1)        #pop删除指定位置元素
print(heros)

heros.clear()     #clear清空列表内容
print(heros)

#改
heros=['钢铁侠', '绿巨人', '黑寡妇', '灭霸', '鹰眼','蜘蛛侠','雷神']
heros[4]='钢铁侠'
print(heros)
heros[3:]=['武松','林冲','李逵']
print(heros)

#排序
nums=[3,4,1,7,5,2,9,8,3]
nums.sort()
print(nums)
nums.reverse()
print(nums)
heros.reverse()
print(heros)

#与先调用sort再调用reverse效果一样
nums=[3,4,1,7,5,2,9,8,3]
nums.sort(reverse=True)
print(nums)

#查
nums=[9, 8, 7, 5, 4, 3, 3, 2, 1]
print(nums.count(3))
heros=['李逵', '林冲', '武松', '黑寡妇', '绿巨人', '钢铁侠']
print(heros.index('绿巨人'))
heros[heros.index('绿巨人')]='神奇女侠'
#若是有多个相同元素，index会返回下标值小的
print(heros)
nums=[9, 8, 7, 5, 4, 3, 3, 2, 1]
print(nums.index(3))
#格式：index(x,start,end)
print(nums.index(3,6,8))


#嵌套列表
s=[1,2,3]
t=[4,5,6]
print(s+t)
print(s*3)
matrix=[[1,2,3],[4,5,6],[7,8,9]]

#访问嵌套列表
for i in matrix:
    for each in i:      #each就是个变量，你可以随便取，a b c d随便什么都行
        print(each,end='\t')
    print()

#创建二维列表
A=[0]*3
for i in range(3):
    A[i]=[0]*3
print(A)

x='FishC'     #字符串是不可变的所以python在内存中只需开辟一个位置
y='FishC'
# is 运算符
print(x is y)

x=[1,2,3]     #列表是可变的，python需要开辟两个位置来存放
y=[1,2,3]
print(x is y)

A=[[0,0,0],[0,0,0],[0,0,0]]
B =[[0]*3]*3
print(B)
A[1][1]=1
print(A)
#[[0, 0, 0], [0, 1, 0], [0, 0, 0]]
B[1][1]=1
print(B)
#[[0, 1, 0], [0, 1, 0], [0, 1, 0]]
print(A[0] is A[1])        #is运算符
#False
print(B[0] is B[1])
#True


#列表推导式
oho=[1,2,3,4,5]
for i in range(len(oho)):
    oho[i]=oho[i]*2
print(oho)
oho=[1,2,3,4,5]
oho=[i * 2 for i in oho]
print(oho)

#列表推导式是一个用于生成新列表的表达式
#基本语法  [expression for item in iterable]
#expression 是基于 item 的某种表达式，iterable 是任何可以遍历的对象
x=[i for i in range(10)]  #for左侧的表达式决定最终输出到列表里的元素
print(x)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
x=[i+1 for i in range(10)]
print(x)
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


x=[]
for i in range(10):
    x.append(i+1)
print(x)

y=[c*2 for c in 'FishC']    #c就是个变量，你可以随便取char,x随便什么都行
print(y)
code=[ord(c) for c in 'FishC']
# ord是个内置函数，作用是将单个字符串转换为对应的ASCII编码
print(code)

matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
col2=[row[1] for row in matrix]   #col=column:列   row就是个变量，你可以随便取a,b,c,d随便什么都行
#看表达式row[1]就知道了，每行的第二个值，分别是2 5 8，最终再组成列表[2, 5 ,8]
print(col2)
diag=[matrix[i][i] for i in range(len(matrix))]
#获得矩阵主对角线元素列表
print(diag)

#循环是通过迭代逐个修改原列表中的元素
#列表推导式则是创建一个新列表，再赋值为原先的变量名
print()
s=[[0]*3 for i in range(3)]
print(s)
s[1][1]=1
print(s)
#列表表达式的高阶运用
#[expression for item in iterable if condition]
#可以添加一个用于筛选的if分句
#先执行for语句，再执行if语句，最后执行左侧表达式
even=[i for i in range(10) if i%2==0]
print(even)
#[0, 2, 4, 6, 8]
even=[i+1 for i in range(10) if i%2==0]
print(even)
#[1, 3, 5, 7, 9]

words =["Great","FishC","Brilliant","Excellent","Fantastic"]
fwords=[w for w in words if w[0]=='F']
print(fwords)

#列表推导式的嵌套
matrix=[[1,2,3],[4,5,6],[7,8,9]]
flatten=[col for row in matrix for col in row]
print(flatten)
flatten=[]
for row in matrix:
    for col in row:
        flatten.append(col)
print(flatten)

product=[x+y for x in 'fishc' for y in 'FISHC' ] #类似于数学中的笛卡尔积 product乘积
print(product)

_=[]
for x in 'fishc':
    for y in 'FISHC':
        _.append(x+y)
print(_)

#列表推导式的终极语法
#每个for语句都能跟一个if语句
print([[x,y] for x in range(10) if x%2==0 for y in range(10) if y%3==0])

_=[]
for x in range(10):
    if x%2==0:
        for y in range(10):
            if y%3==0:
                _.append([x,y])
print(_)



#元组
#元组类型 特点：有序，可重复，不可扩展
rhyme=(1,2,3,4,5,'上山打老虎')
print(rhyme)
rhyme=1,2,3,4,5,'上山打老虎'
print(rhyme)
print(rhyme[0])
print(rhyme[-1])
#元组是不可变的，所以试图修改元组内容的行为是不可取的
#元组可以切片
#列表可以增、删、改、查，元组只能查
nums=(3,4,1,7,5,2,9,8,3)
print(nums.count(3))

heros=('李逵', '林冲', '武松', '黑寡妇', '绿巨人', '钢铁侠')
print(heros.index('绿巨人'))

s=(1,2,3)
t=(4,5,6)
#加号乘号运算符也可以使用
print(s+t)
print(s*3)
#圆括号的必要性
x=(520)
print(type(x))
x=(520,)
print(type(x))
#逗号是本体,构建单一元素的元组：逗号是构成元组的必要条件

#打包:生成一个元组
t=(123,'xiao',3.14)
#解包：将元组中的元素【一次性】赋值给多个变量的做法
#解包适用于任何的【序列】类型
#注意：复制号左边的变量名数量必须跟右侧序列的元素数量一致
x,y,z=t
print(x)
a,b,c,d,e='FISHC'
print(a)
a,b,*c='fishc'
print(c)

#python的多重赋值，原理就是先通过元组打包后解包
x,y=10,20
_=(10,20)
x,y=_
