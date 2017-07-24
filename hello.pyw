#!C:\Users\lf\AppData\Local\Programs\Python\Python36\python3.exe
#!/usr/bin/python3c
#!/usr/bin/env python3
print("hello python")

if True:
    print("True")
else:
    print("False")
    

#  print ("False")    # 缩进不一致，会导致运行错误。统一缩进空格数量即可，不规定缩进几个

# python保留字
import keyword
print(keyword.kwlist)

# 多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
# total = item_one + \
#         item_two + \
#         item_three
# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
# total = ['item_one', 'item_two', 'item_three',
#         'item_four', 'item_five']

# 数据类型
# python中数有四种类型：整数、长整数、浮点数和复数。
# 整数， 如 1
# 长整数 是比较大的整数
# 浮点数 如 1.23、3E-2
# 复数 如 1 + 2j、 1.1 + 2.2j

# 字符串
# python中单引号和双引号使用完全相同。
# 使用三引号('''或""")可以指定一个多行字符串。
# 转义符 '\'
# 自然字符串， 通过在字符串前加r或R。 如 r"this is a line with \n" 则\n会显示，并不是换行。
# python允许处理unicode字符串，加前缀u或U， 如 u"this is an unicode string"。
# 字符串是不可变的。
# 按字面意义级联字符串，如"this " "is " "string"会被自动转换为this is string。
word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
 可以由多行组成"""
print(paragraph)
print(r"this is a line with \n")

# 一行多语句用分号;分割
import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# 不换行输出
x="a"
y="b"
print( x, end=" " )
print( y, end=" " )
print()

# import 与 from...import
# 在 python 用 import 或者 from...import 来导入相应的模块。
# 将整个模块(somemodule)导入，格式为： import somemodule
# 从某个模块中导入某个函数,格式为： from somemodule import somefunction
# 从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
# 将某个模块中的全部函数导入，格式为： from somemodule import *
# 导入 sys 模块
import sys
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)

# 导入 sys 模块的 argv,path 成员
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

# 多个变量赋值
a, b, c, d = 20, 5.5, True, 4+3j
print(type(a), type(b), type(c), type(d))
a = 111
print(isinstance(a, int))

print()
# isinstance 和 type 的区别在于：
class A:
    pass

class B(A):
    pass

print(isinstance(A(), A))  # returns True
print(type(A()) == A)      # returns True
print(isinstance(B(), A))    # returns True
print(type(B()) == A)        # returns False
# 区别就是:
# type()不会认为子类是一种父类类型。
# isinstance()会认为子类是一种父类类型。

print((1+2j)*(1+2j), end=r"""\n\n"""'\n\n')

var1 = 1
var2 = 10
del var1, var2
# print(var1) # NameError: name 'var1' is not defined

print(2 / 4)
print(4 / 2)
print(2 // 4)
print(2 ** 4)


print()
str = 'Runoob'
 
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串


print()
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']

print (list)            # 输出完整列表
print (len(list))            # 
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表


# List (几乎跟JS里的数组一样)
print()
a = [1, 2, 3, 4, 5, 6]
print(a)
a[0] = 9
print(a)
a[2:5] = [13, 14, 15]
print(a)
a[2:5] = []    # 删除(不包含最后一个元素)
print(a)
# append(), pop()


# Tuple 元组（tuple）与列表类似，不同之处在于元组的元素不能修改
print()
tuple = ( 'abcd', 786 , 2.23, 'runoob', 70.2  )
tinytuple = (123, 'runoob', a)
tinytuple1 = ()  # 空元组
tinytuple2 = (456,) # 一个元素，需要在元素后添加逗号
 
print (tuple)             # 输出完整元组
print (tuple[0])          # 输出元组的第一个元素
print (tuple[1:3])        # 输出从第二个元素开始到第三个元素
print (tuple[2:])         # 输出从第三个元素开始的所有元素
print (tinytuple * 2)     # 输出两次元组
print (tuple + tinytuple) # 连接元组


# string、list和tuple都属于sequence（序列）。

# Set 
print()
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}  # 可以使用大括号 { } 或者 set() 函数创建集合，
studen1 = set() # 注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
 
print(student)   # 输出集合，重复的元素被自动去掉
 
# 成员测试
if('Rose' in student) :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
 
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
 
print(a)
 
print("a和b的差集", a - b)     # a和b的差集
 
print("a和b的并集", a | b)     # a和b的并集
 
print("a和b的交集", a & b)     # a和b的交集
 
print("a和b中不同时存在的元素", a ^ b)     # a和b中不同时存在的元素


# Dictionary
print()
dict1 = {}
dict1['one'] = "1 - 菜鸟教程"
dict1[2]     = "2 - 菜鸟工具"
 
tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}
 
 
print (dict1['one'])       # 输出键为 'one' 的值
print (dict1[2])           # 输出键为 2 的值
print (tinydict.keys())   # 输出所有键
print (tinydict.values()) # 输出所有值
print (tinydict)          # 输出完整的字典
tinydict.clear()
print (tinydict)          # 输出完整的字典

d = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])  # 构造函数 dict() 可以直接从键值对序列中构建字典如下：
print(d)


'''
Python数据类型转换
int(x [,base])
将x转换为一个整数
float(x)
将x转换到一个浮点数
complex(real [,imag])
创建一个复数
str(x)
将对象 x 转换为字符串
repr(x)
将对象 x 转换为表达式字符串
eval(str)
用来计算在字符串中的有效Python表达式,并返回一个对象
tuple(s)
将序列 s 转换为一个元组
list(s)
将序列 s 转换为一个列表
set(s)
转换为可变集合
dict(d)
创建一个字典。d 必须是一个序列 (key,value)元组。
frozenset(s)
转换为不可变集合
chr(x)
将一个整数转换为一个字符
unichr(x)
将一个整数转换为Unicode字符
ord(x)
将一个字符转换为它的整数值
hex(x)
将一个整数转换为一个十六进制字符串
oct(x)
将一个整数转换为一个八进制字符串
'''

# Python身份运算符
print()
a = 20
b = 20
 
if ( a is b ):  # 是否同个引用
   print ("1 - a 和 b 有相同的标识")
else:
   print ("1 - a 和 b 没有相同的标识")
 
if ( id(a) == id(b) ):  # id() 函数用于获取对象内存地址
   print ("2 - a 和 b 有相同的标识")
else:
   print ("2 - a 和 b 没有相同的标识")
 
# 修改变量 b 的值
b = 30
if ( a is b ):
   print ("3 - a 和 b 有相同的标识")
else:
   print ("3 - a 和 b 没有相同的标识")
 
if ( a is not b ):
   print ("4 - a 和 b 没有相同的标识")
else:
   print ("4 - a 和 b 有相同的标识")


#
print()
a = 111
b = 222
print(a and b)

#
import random
print(range(10))
print(random.random())
print(random.choice(range(10)))


#
print()
print("=======欢迎进入狗狗年龄对比系统========")
while True:
    try:
        age = int(input("请输入您家狗的年龄:"))
        print(" ")
        age = float(age)
        if age < 0:
            print("您在逗我？")
        elif age == 1:
            print("相当于人类14岁")
            break
        elif age == 2:
            print("相当于人类22岁")
            break
        else:
            human = 22 + (age - 2)*5
            print("相当于人类：",human)
            break
    except ValueError:
        print("输入不合法，请输入有效年龄")


i1 = input("\n\n按下 enter 键后退出。")
print(i1)


