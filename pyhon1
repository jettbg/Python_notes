
#类型转换和input的应用
t_shirt_price=int(input('请输入T-shirt的单价：'))
pants_price=int(input('请输入pants的单价：'))
t_shirt_count=int(input('您买了多少件体恤？'))
pants_count=int(input('您买了多少条裤子？'))
normal_price=t_shirt_price*t_shirt_count+pants_price*pants_count
print(f'normal_price={normal_price}')
discount=0.88
discount_price=normal_price*discount
print(f'discount_price={discount_price}')
'''
请输入T-shirt的单价：45
请输入pants的单价：66
您买了多少件体恤？12
您买了多少条裤子？34
normal_price=2784
discount_price=2449.92 
'''

#三目运算符
#1．定义变量，接收用户的输入
num1= int ( input ('请输入第一个整型数值：'))
num2= int ( input ('请输入第二个整型数值：'))
num3= int ( input ('请输入第三个整型数值：'))
#2．使用三目运算实现两两判断
second_max =num1 if num1>num2 else num2
max= second_max if second_max >num3 else num3
#3．查看结果
print ( f' max ={ max }')
'''
请输入第一个整型数值：33
请输入第二个整型数值：22
请输入第三个整型数值：55
 max =55
'''

#random随机类实现石头剪刀布
# 案例：石头剪刀布
# 1 => 石头，2 => 剪刀，3 => 布

# 1. 先得到电脑出的招数
import random
computer = random.randint(1, 3)
print(f'computer={computer}')

# 2. 提示用户，并输入用户的招数
jett = int(input('请输入您的招数（1：石头，2：剪刀，3：布）:'))

# 3. 判断输赢
# and 的优先级高于 or 的优先级
if (jett == 1 and computer == 2) or (jett == 2 and computer == 3) or (jett == 3 and computer == 1):
    print('我总是能赢的。')
elif (jett == 1 and computer == 3) or (jett == 2 and computer == 1) or (jett == 3 and computer == 2):
    print('电脑赢了。')
else:
    print('平局，不服，再来！')
 

