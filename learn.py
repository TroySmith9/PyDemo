#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("100 + 200 + 300=", 100 + 200 + 300)
print('''line1
line2
... line3''')

print("10 // 3",10 // 3)
print("10 / 3",10 / 3)
print('9 / 3',9 / 3)
print('9 % 3',9 % 3)

# ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
print("ord('A'):", ord('A'))
print("ord('中')", ord('中'))
print("chr(66):", chr(66))
print("chr(25991):", chr(25991))
print("\u4e2d\u6587", '\u4e2d\u6587')
# 10进制转16进制
print("hex(25991):", hex(25991))
# 在bytes中，无法显示为ASCII字符的字节，用\x##显示
print(chr(0x6587), chr(6587))
# 16进制转10进制
print(int('4e2d', 16))
print(int('0x1A', 16))

# 注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节
print('ABC'.encode('ascii'))
print('中文encode','中文'.encode('utf-8'))
# print('中文'.encode('ascii')) #Traceback (most recent call last):

print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))

# 格式化:%s表示用字符串替换，%d表示用整数替换
print('Hello, %s' % 'world')
print('Hi, %s, you have $%d.' % ('Michael', 1000000))
print('%3d-%02d' % (32, 1))  # 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
print('growth rate: %d%%' % 7)  # 转义，用%%来表示一个%

# list
classmates = ['Michael', 'Bob', 'Tracy']
print("classmates[]:", classmates)
print("classmates[0]:", classmates[0])
# print(classmates[3]) #list index out of range
print("classmates[-1]", classmates[-1])  # 可以用-1做索引，直接获取最后一个元素：
print("classmates[-3]", classmates[-3])  # 倒数第3个
# list是一个可变的有序表，所以，可以往list中追加元素到末尾
classmates.append('Adam')
print("classmates:", classmates)
# 把元素插入到指定的位置
classmates.insert(1, "jack")
print("classmates:", classmates)
# 删除list末尾的元素，用pop()
print("classmates.pop:", classmates.pop())
print("classmates:", classmates)
# 删除指定位置的元素，用pop(i)方法
print(classmates.pop(0))

# list元素也可以是另一个list
# s = ['python', 'java', ['asp', 'php'], 'scheme']
p = ['asp', 'php']
s = ['python', 'java', p, 'scheme']
print(s)
print(len(s))

###  tuple----有序列表叫元组,和list非常类似，但是tuple一旦初始化就不能修改 ##
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)
# 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (2,)
print(t)

# 变的不是tuple的元素，而是list的元素
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print("tuple:",t)

####if Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做
age = 3
if age >= 18:
    print('your age is', age)
    print('adult')
elif age > 5:
    print("child")
    print(age)
else:
    print("baby")

height = 1.65
weight = 70
bmi = weight / height.__mul__(height)
print("bmi", bmi)
if bmi < 18.5:
    print("过轻")
elif bmi < 25:
    print("正常")
elif bmi < 28:
    print("过重")
else:
    print("肥胖")

print(height.__mul__(height).__mul__(21.75))

### input
# s = input('birth: ')
# birth = int(s)  #input()返回的数据类型是str
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')

##  循环  ##  for 与 while
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

# range()函数，可以生成一个整数序列
sum = 0
# 生成0-100的整数序列
for x in range(101):
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 1
print(sum)

# break 与 continue 含义不变

### dict-字典 类似map ###
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])  # 如果key不存在，dict就会报错
print("d.get('Michael')", d.get('Michael'))
# in判断key是否存在
print('Michael' in d, 'Thomas' in d)
# 删除
d.pop("Bob")
print(d)

## set
s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
s.remove(2)
print(s)
# 集合运算
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)

## 数据类型转换 ##
print(int(1.23))
str = "258"
print(int(str))
print(int(float('3.23')))


## 定义函数 ##  from learn import my_abs来导入my_abs()函数，learn（不含.py扩展名）
def my_abs(x):
    if not isinstance(x, (int, float)):
        # raise TypeError('bad operand type')
        # pass
        return x
    if x >= 0:
        return x
    else:
        return -x


# 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None, return None简写为return
# 空函数------什么事也不做的空函数，可以用pass语句

print(my_abs(-5.3))
print(my_abs("daf"))

# 返回多个值
import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 45, math.pi / 6)
print(x, y)
r = move(100, 100, 45, math.pi / 6)  # 返回值是一个tuple，一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值
print(r)


def power(x, n=2):  # 默认参数(选参数在前，默认参数在后)
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 3))
print(power(5))


def add_end(L=None):  # L = []会出现['END', 'END'] --->默认参数必须指向不变对象
    if L is None:
        L = []
    L.append('END')
    return L


print(add_end())
print(add_end())


#
def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc([1, 2, 3]))  # list
print(calc((1, 3, 5, 7)))  # tuple


# 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去可以传入任意个参数，包括0个参数
def calc2(*nums):
    sum = 0
    for n in nums:
        sum = sum + n * n
    return sum


print(calc2(1, 2, 3))  # list
print(calc2(1, 3, 5, 7))  # tuple


# 关键字参数--可以传入任意不受限制的关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Adam', 45, gender='M', job='Engineer')


# 限制关键字参数的名字
def person(name, age, *, city, job):  # 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
    print(name, age, city, job)


person('Jack', 24, city='Beijing', job='Engineer')
# person('Jack', 24, city='Beijing') # Eroor
# person('Jack', 24, 'Beijing', 'Engineer') # Eroor

L = list(range(10))
# L = range(10)
print(L)
print(L[:5])
print(L[2:5])
print(L[:5:3])

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)