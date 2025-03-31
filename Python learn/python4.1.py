#创建和调用函数
def myfunc():
    pass     #函数体
myfunc()
def myfunc():
    for i in range(3):
        print('hhh')
myfunc()
#函数的参数
def myfunc(name):
    for i in range(3):
        print(f'hh{name}')
myfunc('p')

def myfunc(name,times):
    for i in range(times):
        print(f'hh{name}')
myfunc('w',2)
#形式参数和实际参数
#函数返回值
def div(x,y):
    z=x/y
    return z  #或者return x/y
print(div(4,2))

def div(x,y):
    if y==0:
        return '除数不能为0'
    else:
      return x/y
print(div(4,0))

def myfunc():
    pass
print(myfunc())
#位置参数
def myfunc(a,b,c):
    return''.join((c,b,a))
#join() 是一个字符串方法，用于将一个可迭代对象（如列表、元组、集合等）中的元素连接成一个字符串
print(myfunc('你','是','我'))
#关键字参数
print(myfunc(a='我',b='是',c='你'))
#位置参数必须在关键字参数之前
#print(myfunc(a='我','清蒸','你'))  这样会报错
#默认参数
def myfunc(a,b,c='你'):
    return ''.join((c,b,a))
print(myfunc('西瓜','吃'))
print(myfunc('西瓜','吃','我'))
#默认参数要定义在后面
#def myfunc(a='西瓜',b,c='你'):
#    return ''.join((c,b,a))   这样会报错，应该
def myfunc(a,b='西瓜',c='你'):
     return ''.join((c,b,a))   

#help()函数  查看函数或模块用途的详细说明
help(abs)     #abs用于计算一个数的绝对值
#abs(x, /)   
#   Return the absolute value of the argument.
#斜杠左侧不能使用关键字参数，只能使用位置参数 abs(x=-1.5)是错误的
#斜杠右侧随意
print(abs(-1.5))
help(sum)
#sum(iterable, /, start=0)
print(sum([1,2,3],4))
print(sum([1,2,3],start=4))

#自己定义函数
def abc(a,/,b,c):
    print(a,b,c)
abc(1,2,3)

def abc(a,*,b,c):  #*左侧可以是位置参数或关键字参数 右侧只能是关键字参数
    print(a,b,c)

#收集参数  将想传入几个就传几个的形参称之为收集参数
def myfunc(*args):
    print('有{}个参数'.format(len(args)))
    print('第二个参数是{}'.format(args[1]))
myfunc(1,23,4,2,1)

#1.打包为元组
def myfunc(*args):
    print(args)
myfunc(1,2,34,5)
#输出为(1, 2, 34, 5)  背后立功的是元组，元组具有打包和解包的功能，这一个功能就运用到了函数里面。
#函数可以返回多个值
def myfunc():
    return 1,2,3
print(myfunc())
#返回多个值python其实是用了元组进行了打包的。

#如果在收集参数后面还需要指定其它参数时，在调用函数时就需要使用关键字参数来指定后面的参数，否则这些实参数都会被认为是收集参数
def myfunc(*args,a,b):
    print(args,a,b)
#myfunc(1,2,3,4,5)这样会报错，报错的大意是说缺少了a和b这两个参数的实参
myfunc(1,2,3,a=4,b=5)

#2.将多个参数打包为字典
def myfunc(**kwargs):
    print(kwargs)
myfunc(a=1,b=2,c=3)  #这个时候实参就必须得是关键字参数了

#还可以混合起来使用
def myfunc(a,*b,**c):
    print(a,b,c)
myfunc(1,2,3,4,x=5,y=6)
#结果为1 (2, 3, 4) {'x': 5, 'y': 6}  注意手机参数要放在后面

#之前使用的help函数就是同时使用这两种收集参数的
help(str.format)  #str.format 是字符串对象所具备的一个方法，它可以用来格式化字符串。
#format(self, /, *args, **kwargs)

#3.解包函数  *号在形参的应用就是打包参数，而在实参上的应用就是解包参数
args=(1,2,3,4)
def myfunc(a,b,c,d):
    print(a,b,c,d)
#myfunc(args) 这样会报错，args是一个元组相当于一个实参，报错中显示b，c和d这三个形参没有实参传入进去
myfunc(*args)  #加上*解包就好了
kwargs={'a':1,'b':2,'c':3,'d':4}
myfunc(**kwargs)  #**表示解包字典，字典解包的是键值




    
 
