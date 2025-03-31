#字符串 
#字符串的根本是序列，像元组那样不可变的序列
x='12321'
'是回文数' if x==x[::-1] else '不是回文数'


#1.大小写字母换来换去 

#capitalize()将字符串的首字母变成大写，其它字母变成小写，
#注意使用该方法后返回的不是原字符串，因为字符串是不可变的对象，它只是按照这个规则来形成一个新的字符串。

#casefold()是返回一个所有字母都是小写的新字符串。
#title()会将字符串的每个单词的首字母都变成大写，该单词的所有其它字母都变成小字母。
#swapcase() 会将字符串中的所有字母大小写翻转。
#upper()是将所有的字母都变成大写。
#lower()是将所有的字母都变成小写。

#lower()与casefold()是有区别的，lower()只能处理英文字符，而casefold()除了可以处理英文之外，还可以处理其它字符例如德语等。 


#2.左中右对齐 
#这四个方法都有一个 width 参数，用来指定整个字符串的宽度，如果说指定的宽度小于或者等于原字符串那就别提什么对齐了，直接原字符串输出。
# center(width, fillchar=’’)    
#center(width, fillchar=’’)按照你给的宽度把源字符串放在中间，居中对齐，左右两侧默认用空格填充。

# ljust(width, fillchar=’’)   
# rjust(width, fillchar=’’)   
#ljust(width, fillchar=’’)实现的是左对齐，rjust(width, fillchar=’’)实现的是右对齐，同样剩余的宽度，默认用空格去填充。

# zfill(width) 
#zfill(width)比较特殊，它是右对齐，左侧填充0，这个在做数据报表的时候会比较实用，对于数字而言它也可以机智的处理带负号的数字。

#左中右对齐的方法还支持一个叫fillchar的参数，它的默认值是空格，你不去设置它，就会用空格去填充，同样也可以给它填充想添加的字符,不过只能填充一个字符。 


#3.查找 
# count(sub[,start[,end]])   
# count方法用于找出sub参数指定的子字符串在字符串中出现的次数，start和end用于查找指定的起始和结束位置，位置是各个字符对应的数字位置下标索引值，下标的标记方法和列表一样。 

# find(sub[,start[,end]])    
# rfind(sub[,start[,end]]) 
#find 和 rfind 的作用是查找sub参数所指定的子字符串所对应的下标索引值，它们的区别是前置是从左往右找，后者是从右往左找，
#若查找的子字符串比较多的话，默认只查找第一个对应的下标索引值。
# index(sub[,start[,end]])   
# rindex(sub[,start[,end]])
#index 和 rindex 这两个方法和 find 的两个方法是很相似的，
#它们的区别是如果定位不到子字符串，它们的处理方式是不一样的，find和rfind找不到的话它返回的是-1，index它找不到的话是会抛出异常的。


#4.替换 
#expandtabs（[tabsize=8]）
# expandtabs 这个方法是使用空格来代替换制表符，并且呢返回一个新的字符
code ='''
        print (" I love fishc ")
    print ("我爱中国") '''
new_code=code.expandtabs(4) 
#使用 expandtabs 就可以将字符串中的Tab全部替换成空格,（）里的参数是指定一个Tab等于多少个空格。 
print(new_code)

#replace(old,new,count=-1)
#replace 是将old参数指定的旧字符串替换成new参数指定的新字符串，
#count参数指定的是替换的次数，count的默认值是-1，也就是说你不设置这个参数的话，它就相当于全部替换：     
'你好，再见'.replace('再见','想你')
'再见，再见'.replace('再见','想你',1)
'再见，再见'.replace('再见','想你',-1)

#translate(table) 
#translate(table)这个方法是返回一个根据 table 参数转换后的新字符串，
#table 在这里是表格的意思，由于指定一个转换规则的表格，
#这个转换规则的表格是如何得到的？怎么生成的呢？
#需要用到一个str.maketrans(x[,y[,z]]): 
table=str.maketrans('ABCDEFG','1234567')
'I love FishC'.translate(table)
#输出结果 'I love 6ish3'

#str.maketransz()这是属于字符串的一个静态方法。我们建立一个表格将“ABCDEFG”替换成“1234567”，然后把这个表格放到到一个变量名中去，给它起名 table，
#之后直接把这个变量给到 translate()里面的参数。也可以不用赋值给一个变量名直接把这个转换规则放到 translate()的参数里边。

#此外这个 str.maketrans()方法还支持第三个参数，表示将指定的字符串给忽略
table=str.maketrans('ABCDEFG','1234567','love')
'I love FishC'.translate(table)
#输出结果为 'I 6ish3'


#5.判断和检测 
#一共14种方法，都是对应字符串各种情况下的判断和检测，所以返回的都是布尔类型的值，要么就是true，要么就是false。 

x ="我爱Pyhon"
x.startswith ("我爱") 
#True 
#startswith(prefix[,start[,rnd]])这个方法用来判断这个参数指定的子字符串是否出现在字符串的起始位置。
x.endswith (" hon ") 
#True 
#endswith(suffix[,start[,end]])这个方法用来判断参数指定的子字符串是否出现在字符串末尾的地方。

#这两个方法里都有方括号里面写着start和end，这个方括号说明这是一个可选参数，它就相当于这个函数或者方法的一个高级定制版本，我们如果给它赋值的话它会有新的特性 
x.startswith ("我",1) 
#False 
x.startswith ("爱",1) 
#True 
x.endswith (" Py ",0,4) 
#True

#此外方括号里面的参数其实是支持以元组的形式传入多个待匹配的字符串的：
x='她爱Python'
if x.startswith(('你','我','她')):
    print('总有人爱Python')
#这个元组可以提供任何你觉得有可能匹配成功的元素进去，只要有一个匹配成功那么它就返回 True，这里注意 startswith 后要有两个括号。 

#istitle()可以判断一个字符串中所有单词是否都是以大写字母开头，其余字母均为小写，
#isupper()方法可以判断一个字符串中是否所有的字母都是大写
#islower()判断一个字符串中是否全部为小写。
 
#在一个语句中连续调用两个方法，Python会从左往右依次进行调用：
x.upper().isupper() 

#isalpha()方法可以用来判断字符串中是否只有字母构成，注意空格不是字母哦。
#isspace()可以用来判断是否是空白字符串，注意并不是只有空格是空白字符串Tab以及转义字符\n等也都是空白字符。
#isprintable()可以用来判断一个字符串中是否所有字符都是可打印的，注意转义字符\n 不是一个可打印字符。 

#isdecimal()，isdigit()，isnumeric()这几个方法都是用来判断数字的。
#isdecimal()用来判断是否只包含十进制字符，例如2²就不行。
#isdigit()可以用来判断是否是数字，其它进制的数字也可以，例如 2²的返回值就是 True，但是罗马数字、汉字的数字就不行了。
#而这些罗马数字、汉字用isnumeric()方法的返回值就是True了。 
#isalnum()是一个集大成者，只要 isalpha()、isdecimal()，isdigit()，isnumeric()任意一个返回值是True 它的返回值就是 True。
#isidentifier()用来判断字符串是否是一个 Python 合法的标识符，比如变量名必须得是一个合法的标识符 

#判断一个字符串是否为Python的保留标识符，就像 if、while，for 这些关键字，可以使用 keyword 模块的 iskeyword 函数来进行实现
import keyword 
keyword . iskeyword (" if ")
#keywore.iskeyword()的意思是说调用 keyword模块里的iskeyword函数
#True 
keyword . iskeyword (" python ") 
#False

#6.截取 
'''
strip(chars=None)    lstrip(chars=None)    rstrip(chars=None) 
removeprefix(prefix)    removesuffix(suffix) '
'''

#7.拆分和拼接 

#8.格式化字符串 
year=1010
print('工作室成立于{}年'.format(year))
#使用一对花括号来表示替换字段，也就是真正的内容是放在format()方法的参数中

#用索引值索引
print('{}看到{}很激动'.format('我','你'))
print('{1}看到{0}很激动'.format('我','你'))
print('{0}{0}{1}{1}'.format('是','非'))

#除了索引值进行索引，format()方法也可以通过关键字精确索引、
print('我是{name},我爱{0},{0}不爱{name}'.format('Python',name='dxy'))
#注意虽然关键字和索引值都可以索引，但要把索引值的参数放在前面，关键字放在后面，且关键字没有下标索引值。 

#在格式化字符串中花括号的作用是占位的，那么要单纯的输入一对花括号的话可以直接在参数里直接写上花括号，因为花括号也是一个字符串
print('{},{},{}'.format(1,'{}',2))
#结果为 '1,{},2'

#此外还可以使用花括号来注释花括号（即在花括号里写入花括号）
print('{},{{}},{}'.format(1,2))
#'1,{},2'
 
#9.f-字符串（f-string） 
#语法糖是一个计算机术语，是指计算机语言中添加的某种语法，这种语法对语言的功能没有影响，但是更方便程序员使用，语法糖让程序更加简洁，有更高的可读性。
year=2020
print(f'工作室成立于{year}年')
