# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# import builtins
# import os
# from collections import Iterator
#
# print("100 + 200 + 300=", 100 + 200 + 300)
# print('''line1
# line2
# ... line3''')
#
# print("10 // 3", 10 // 3)
# print("10 / 3", 10 / 3)
# print('9 / 3', 9 / 3)
# print('9 % 3', 9 % 3)
#
# # ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
# print("ord('A'):", ord('A'))
# print("ord('中')", ord('中'))
# print("chr(66):", chr(66))
# print("chr(25991):", chr(25991))
# print("\u4e2d\u6587", '\u4e2d\u6587')
# # 10进制转16进制
# print("hex(25991):", hex(25991))
# # 在bytes中，无法显示为ASCII字符的字节，用\x##显示
# print(chr(0x6587), chr(6587))
# # 16进制转10进制
# print(int('4e2d', 16))
# print(int('0x1A', 16))
#
# # 注意区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但bytes的每个字符都只占用一个字节
# print('ABC'.encode('ascii'))
# print('中文encode', '中文'.encode('utf-8'))
# # print('中文'.encode('ascii')) #Traceback (most recent call last):
#
# print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
#
# # 格式化:%s表示用字符串替换，%d表示用整数替换
# print('Hello, %s' % 'world')
# print('Hi, %s, you have $%d.' % ('Michael', 1000000))
# print('%3d-%02d' % (32, 1))  # 格式化整数和浮点数还可以指定是否补0和整数与小数的位数
# print('growth rate: %d%%' % 7)  # 转义，用%%来表示一个%
#
# # list
# classmates = ['Michael', 'Bob', 'Tracy']
# print("classmates[]:", classmates)
# print("classmates[0]:", classmates[0])
# # print(classmates[3]) #list index out of range
# print("classmates[-1]", classmates[-1])  # 可以用-1做索引，直接获取最后一个元素：
# print("classmates[-3]", classmates[-3])  # 倒数第3个
# # list是一个可变的有序表，所以，可以往list中追加元素到末尾
# classmates.append('Adam')
# print("classmates:", classmates)
# # 把元素插入到指定的位置
# classmates.insert(1, "jack")
# print("classmates:", classmates)
# # 删除list末尾的元素，用pop()
# print("classmates.pop:", classmates.pop())
# print("classmates:", classmates)
# # 删除指定位置的元素，用pop(i)方法
# print(classmates.pop(0))
#
# # list元素也可以是另一个list
# # s = ['python', 'java', ['asp', 'php'], 'scheme']
# p = ['asp', 'php']
# s = ['python', 'java', p, 'scheme']
# print(s)
# print(len(s))
#
# ##  tuple----有序列表叫元组,和list非常类似，但是tuple一旦初始化就不能修改 ##
# classmates = ('Michael', 'Bob', 'Tracy')
# print(classmates)
# # 只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
# t = (2,)
# print(t)
#
# # 变的不是tuple的元素，而是list的元素
# t = ('a', 'b', ['A', 'B'])
# t[2][0] = 'X'
# t[2][1] = 'Y'
# print("tuple:", t)
#
# ####if Python的缩进规则，如果if语句判断是True，就把缩进的两行print语句执行了，否则，什么也不做
# age = 3
# if age >= 18:
#     print('your age is', age)
#     print('adult')
# elif age > 5:
#     print("child")
#     print(age)
# else:
#     print("baby")
#
# height = 1.65
# weight = 70
# bmi = weight / height.__mul__(height)
# print("bmi", bmi)
# if bmi < 18.5:
#     print("过轻")
# elif bmi < 25:
#     print("正常")
# elif bmi < 28:
#     print("过重")
# else:
#     print("肥胖")
#
# print(height.__mul__(height).__mul__(21.75))
#
# ## input
# # s = input('birth: ')
# # birth = int(s)  #input()返回的数据类型是str
# # if birth < 2000:
# #     print('00前')
# # else:
# #     print('00后')
#
# #  循环  #  for 与 while
# names = ['Michael', 'Bob', 'Tracy']
# for name in names:
#     print(name)
#
# # range()函数，可以生成一个整数序列
# sum = 0
# # 生成0-100的整数序列
# for x in range(101):
#     sum = sum + x
# print(sum)
#
# sum = 0
# n = 99
# while n > 0:
#     sum = sum + n
#     n = n - 1
# print(sum)
#
# # break 与 continue 含义不变
#
# ## dict-字典 类似map ###
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'])  # 如果key不存在，dict就会报错
# print("d.get('Michael')", d.get('Michael'))
# # in判断key是否存在
# print('Michael' in d, 'Thomas' in d)
# # 删除
# d.pop("Bob")
# print(d)
#
# # set
# s = set([1, 2, 3])
# print(s)
# s.add(4)
# print(s)
# s.remove(2)
# print(s)
# # 集合运算
# s1 = set([1, 2, 3])
# s2 = set([2, 3, 4])
# print(s1 & s2)
# print(s1 | s2)
#
# # 数据类型转换 ##
# print(int(1.23))
# string = "258"
# print(int(string))
# print(int(float('3.23')))
#
#
# # 定义函数 #  from learn import my_abs来导入my_abs()函数，learn（不含.py扩展名）
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         # raise TypeError('bad operand type')
#         # pass
#         return x
#     if x >= 0:
#         return x
#     else:
#         return -x
#
#
# # 如果没有return语句，函数执行完毕后也会返回结果，只是结果为None, return None简写为return
# # 空函数------什么事也不做的空函数，可以用pass语句
#
# print(my_abs(-5.3))
# print(my_abs("daf"))
#
# # 返回多个值
# import math
#
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
#
#
# x, y = move(100, 100, 45, math.pi / 6)
# print(x, y)
# r = move(100, 100, 45, math.pi / 6)  # 返回值是一个tuple，一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值
# print(r)
#
#
# def power(x, n=2):  # 默认参数(选参数在前，默认参数在后)
#     s = 1
#     while n > 0:
#         n = n - 1
#         s = s * x
#     return s
#
#
# print(power(5, 3))
# print(power(5))
#
#
# def add_end(L=None):  # L = []会出现['END', 'END'] --->默认参数必须指向不变对象
#     if L is None:
#         L = []
#     L.append('END')
#     return L
#
#
# print(add_end())
# print(add_end())
#
#
# #
# def calc(numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
#
#
# print(calc([1, 2, 3]))  # list
# print(calc((1, 3, 5, 7)))  # tuple
#
#
# # 在list或tuple前面加一个*号，把list或tuple的元素变成可变参数传进去可以传入任意个参数，包括0个参数
# def calc2(*nums):
#     sum = 0
#     for n in nums:
#         sum = sum + n * n
#     return sum
#
#
# print(calc2(1, 2, 3))  # list
# print(calc2(1, 3, 5, 7))  # tuple
#
#
# # 关键字参数--可以传入任意不受限制的关键字参数
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
#
# person('Michael', 30)
# person('Bob', 35, city='Beijing')
# person('Adam', 45, gender='M', job='Engineer')
#
#
# # 限制关键字参数的名字
# def person(name, age, *, city, job):  # 命名关键字参数需要一个特殊分隔符*，*后面的参数被视为命名关键字参数
#     print(name, age, city, job)
#
#
# person('Jack', 24, city='Beijing', job='Engineer')
# # person('Jack', 24, city='Beijing') # Eroor
# # person('Jack', 24, 'Beijing', 'Engineer') # Eroor
#
# L = list(range(10))
# # L = range(10)
# print(L)
# print(L[:5])
# print(L[2:5])
# print(L[:5:3])
#
# d = {'a': 1, 'b': 2, 'c': 3}
# for key in d:
#     print(key)
#
# # 列表生成式
# print(list(range(1, 11)))
# print([x * x for x in range(1, 11)])
# print([x * x for x in range(1, 11) if x % 2 == 0])
# # 两层循环，可以生成全排列
# print([m + n for m in 'ABC' for n in 'XYZ'])
# print([d for d in os.listdir('.')])  # os.listdir可以列出文件和目录
# d = {'x': 'A', 'y': 'B', 'z': 'C'}
# for k, v in d.items():
#     print(k, '=', v)
#
# # 生成器 ::一边循环一边计算的机制，称为生成器：generator
# # 1. 。第一种方法很简单，只要把一个列表生成式的[]改成()，就创建了一个generator：
# L = [x * x for x in range(10)]
# print(L)
# g = (x * x for x in range(10))
# print(g)
#
# n = 0
# # while n < 5:
# #     print("next:",next(g))
# #     n = n + 1
#
# for x in g:
#     print("for:", x)
#
# for ch in 'ABC':
#     print(ch)
#
# # 斐波拉契数列
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)  # 要把print(b)改为yield b就可以 把fib函数变成generator. 每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# fib(10)
#
#
# #  杨辉三角
# def triangles():
#     pre = [1]
#     now = [1]
#     while True:
#         yield now
#         for x in range(1, len(pre)):
#             now[x] = pre[x] + pre[x - 1]
#         now.append(1)
#         pre = list(now)
#     return 'done'
#
#
# n = 0
# for t in triangles():
#     print(t)
#     n = n + 1
#     if n == 10:
#         break
#
#
# # 2
# def triangles2():
#     L = [1]
#     while True:
#         yield L
#         L.append(0)  # 补完0后L的状态 [1,0]
#         L = [L[i - 1] + L[i] for i in range(len(L))]
#         if len(L) > 10:  # 仅输出10行
#             break
#     return L
#
#
# a = triangles2()
# for i in a:
#     print(i)
#
# # 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
# print("isinstance([], Iterator)：", isinstance([], Iterator))
#
# # 把list、dict、str等Iterable变成Iterator可以使用iter()函数
# print("isinstance(iter([]), Iterator)", isinstance(iter([]), Iterator))
#
# # 函数式编程--Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言
# # 变量可以指向函数
# f = abs
# print(f(-10))
#
# abs = -10
# # abs(-10)
# print(builtins.abs(abs))
#
#
# def add(x, y, f):
#     return f(x) + f(y)
#
#
# x = -5
# y = 6
# f = builtins.abs
# print(f(x) + f(y))
#
#
# # map/reduce
# # map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回
#
# def normalize(name):
#     s = name[0].upper() + name[1:].lower()
#     return (s)
#
#
# L1 = ['adam', 'LISA', 'barT']
# print(list(map(normalize, L1)))
# print(list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
#
# # # reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# def fn(x, y):
#     return x * 10 + y
#
# print(fn(1,2))
# # print(list(map(fn, [1, 3, 5, 7, 9]))) TODO  TypeError: 'int' object is not iterable  ??
#
#
# # filter 用于过滤序列: 接收一个函数和一个序列-把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素
#
# # 一个list中，删掉偶数，只保留奇数
# def is_odd(n):
#     return n % 2 == 1
#
# print(list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])))
#
# # 一个序列中的空字符串删掉
# def not_empty(s):
#     return s and s.strip()
#
# print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))
#
# # 得到所有的素数
#
#
# # sorted
#
# # Python内置的sorted()函数
# print(sorted([36, 5, -12, 9, -21]))
#
# # sorted()函数也是一个高阶函数，它还可以接收一个key函数来实现自定义的排序
# import builtins
#
# print(sorted([36, 5, -12, 9, -21], key=builtins.abs))
# # 忽略大小写的排序
# print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
#
# # 成绩从高到低排序：
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_sort(t):
#     return t[1]
# def by_name(t):
#     return t[0]
# print(sorted(L,key=by_sort))
# print(sorted(L,key=by_name))
#
# print(by_name.__name__,by_name.__annotations__,by_name.__class__,by_name.__closure__)

# 装饰器_ 函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）

# def log(func):
#     def wrapper(*args, **kw):
#         print('before call %s():' % func.__name__)
#         k = func(*args, **kw)
#         print('after call %s():' % func.__name__)
#         return k
#
#     return wrapper
#
#
# @log
# def now():
#     print("now")
#
#
# now()
#
#
# def log(text):
#     def decorator(func):
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator
#
#
# @log('execute')
# def now():
#     print('2015-3-25')
#
#
# now()

# # 偏函数
# print(int('12345', base=8))
#
# # 使用模块
#
#
#
# import sys
#
#
# def test():
#     args = sys.argv
#     if len(args) == 1:
#         print('Hello, world!')
#     elif len(args) == 2:
#         print('Hello, %s!' % args[1])
#     else:
#         print('Too many arguments!')
#
#
# print(__name__, test.__annotations__)
#
# if __name__ == '__main__':
#     test()


# 面向对象
# 类和实例
# class Student(object):
#     pass
#
#
# bart = Student()
# print(bart)
#
# bart.name = 'Bart Simpson'
# print(bart.name)
#
# class Student(object):
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score


# 访问限制--让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
# class Student(object):
#     def __init__(self, name, score):
#         self.__name = name
#         self.__score = score
#
#     def print_score(self):
#         print('%s: %s' % (self.__name, self.__score))
#
#     def get_name(self):
#         return self.__name
#
#     def get_score(self):
#         return self.__score
#
#     def set_score(self, score):
#         self.__score = score


# 变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名


# 继承和多态

# class Animal(object):
#     def run(self):
#         print('Animal is running...')
#
#
# class Dog(Animal):
#     def run(self):
#         print('Dog is running...')
#
#
# class Cat(Animal):
#     def eat(self):
#         print('Eating meat...')
#
#
# dog = Dog()
# dog.run()
#
# cat = Cat()
# cat.run()
# cat.eat()
#
# an = Animal()
#
#
# def run_twice(animal):
#     animal.run()
#
#
# print("isinstance(dog,Dog):", isinstance(dog, Dog), "isinstance(dog,Animal):", isinstance(dog, Animal),
#       "isinstance(an,Dog):", isinstance(an, Dog))
#
# run_twice(Dog())
# # run_twice(Cat())
#
#
# # 于Python这样的动态语言来说，则不一定需要传入Animal类型。我们只需要保证传入的对象有一个run()方法就可以了
# class Timer(object):
#     def run(self):
#         print("Time run……")


# run_twice(Timer())
#
#
# print(type(123),type('abc'))
# 可以判断一个变量是否是某些类型中的一种
# print("isinstance([1, 2, 3], (list, tuple)):",isinstance([1, 2, 3], (list, tuple)))
# print("isinstance((1, 2, 3), (list, tuple)):",isinstance((1, 2, 3), (list, tuple)))
# print(isinstance("a",(str,int)))

# dir()-获得一个对象的所有属性和方法
# print("dir('abc')", dir('abc'))
#
# print("abc".__add__("d"))
#
#
# class Student(object):
#     def set_age(self, age):  # 定义一个函数作为实例方法
#         self.age = age
#
#
# s = Student()
# s.set_age(25)

# print(s.age)

# __slots__:  要限制实例的属性


# class Student(object):
#     __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称
#
#
# s = Student()  # 创建新的实例
# s.name = 'Michael'  # 绑定属性'name'
# s.age = 25  # 绑定属性'age'


# s.score = 99 # 绑定属性'score'
# AttributeError: 'Student' object has no attribute 'score'


# @property  :把一个getter方法变成属性，只需要加上@property就可以了

# class Student(object):
#     @property
#     def birth(self):
#         return self._birth
#
#     @birth.setter
#     def birth(self, value):
#         self._birth = value
#
#     @property
#     def age(self):
#         return 2017 - self._birth


# 多重继承

# class Runnable(object):
#     def run(self):
#         print('Running...')
#
#
# class Flyable(object):
#     def fly(self):
#         print('Flying...')
#
#
# class Animal(object):
#     pass
#
#
# # 大类:
# class Mammal(Animal):
#     def eat(self):
#         print("eating ……")
#
#
# class Bird(Animal):
#     pass
#
#
# # 通过多重继承，一个子类就可以同时获得多个父类的所有功能
# class Dog(Mammal, Runnable):
#     pass
#
#
# dog = Dog()
# dog.run()
# dog.eat()



# class Student(object):
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return 'Student object (name: %s)' % self.name
#
#
# stu = Student("Python")
# print(stu)
#
#
# # __iter__
# class Fib(object):
#     def __init__(self):
#         self.a, self.b = 0, 1  # 初始化两个计数器a，b
#
#     def __iter__(self):
#         return self  # 实例本身就是迭代对象，故返回自己
#
#     # 返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()    方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环
#     def __next__(self):
#         self.a, self.b = self.b, self.a + self.b  # 计算下一个值
#         if self.a > 100000:  # 退出循环的条件
#             raise StopIteration();
#         return self.a  # 返回下一个值
#
#     # __getitem__():像list那样按照下标取出元素
#     def __getitem__(self, n):
#         a, b = 1, 1
#         for x in range(n):
#             a, b = b, a + b
#         return a
#
#
# # for n in Fib():
# #     print(n)
#
# f = Fib()
# print(list(f))
# print(f[10])


# 枚举类
# from enum import Enum
#
# 方法1：好处是简单，缺点是类型是int，并且仍然是变量
# Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# for name, member in Month.__members__.items():
#     print(name, '=>', member, ',', member.value)


# # 方法2：更精确地控制枚举类型，可以从Enum派生出自定义类
# from enum import Enum, unique
#
#
# @unique  # @unique装饰器可以帮助我们检查保证没有重复值。
# class Weekday(Enum):
#     Sun = 0  # Sun的value被设定为0
#     Mon = 1
#     Tue = 2
#     Wed = 3
#     Thu = 4
#     Fri = 5
#     Sat = 6
#
#
# day1 = Weekday.Mon
# print(day1, "->", day1.value)
# print(Weekday.Tue.value, "->", Weekday['Tue'])


# 错误处理 try except finally ; Python的错误其实也是class，所有的错误类型都继承自BaseException

# try:
#     print('try...')
#     r = 10 / 0
#     print('result:', r)
# except ZeroDivisionError as e:
#     print('except:', e)
# finally:
#     print('finally...')
# print('END')


# 调试
# 1. print()
# 2.断言 _凡是用print()来辅助查看的地方，都可以用断言（assert）来替代
# 3.logging
import logging


def foo(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    logging.info('n = %d' % n)
    return 10 / n


# def main():
print(foo('1'))

# 单元测试


