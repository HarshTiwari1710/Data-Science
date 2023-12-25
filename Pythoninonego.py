'''data Types'''
# #int
# a = 23456
# b = -9853
# #float
# f1 = 8.4567
# f2 = -0.6785
# #string
# str1 = 'Jello'
# #bool
# b1 = True
# b2 = False
# #output
# print(a,b1)
# #variable 
# hello = 20
# print(hello) 
# Name = input('Name :')
# Age = input('Age: ')
# print('Hello', Name, 'you are', Age, 'years old')
'''arithemic operators'''
# x = 9
# Y = 5
# result= x %Y *2
# print (result)
# num = int(input('Number: '))
# print(num - 5)
'''string operators'''
# str1 = 'hello'
# print(type(str1))
# print(str1.upper())
# print(str1.lower())
# print(str1.capitalize())
# print(str1.count('l'))
# x = 'harsh'
# y = 'yes'
# print(x + y)
'''conditional operators'''
# """
# Value is either true or False
# ==
# !=
# <=
# >=
# <
# >
# """
# x = 'hello'
# y = 'hello'
# print('ab'>'ad')
# print(ord('z'))
# print(7.0==7)
'''chained condition'''
# x =7
# y=8
# z=0
# res1 = x==y
# res2 = y>x
# res3 = z<x+2
# '''and
# or
# not'''
# res4 = res1 or not res2 or res3 
#if else-if else conditions
# x = 10

# if x < 0:
#     print("x is negative")
# elif x == 0:
#     print("x is zero")
# else:
#     print("x is positive")
#list
# x = [4,True,'hi']
# print(len(x))
# y = 'hi'
# print(len(y))
# x.extend([4,5,6,7,8,9])
# print(x)
# print(x.pop(0))
# print(x[2])
# x[0] = 'hello'
# print(x)

'''Tuple'''
# x = (0,0,2,2)
# print(x[0])

'''for and while loop'''
# for i in range(11):
#     print(i)
# # range has = start, stop and step
#     if(i==10):
#         print('I have one toffee') 

# for i in range(10, -1,-1):
#     print(i)  
# x =[3,5,6,8,9,7,2,30]
# for i in range(len(x)):
#     print(x[i])
# for i,element in enumerate(x):
#     print(i,element)
# i = 0
# while i<10:
#     print('run')
#     i+=1
#     print(i)
'''slicing operator'''
# x = [0,1,2,3,4,5,6,7,8]
# y = ['hi', 'hello', 'goodbye', 'cya', 'sure']
# s = 'hello'
# sliced = s[::2]
# print(sliced)
#Works on tuples as well
'''sets'''
# x = set()
# s = {4,32,2,2}
# s.add(5)
# s.remove(2)
# s2 = {4,32,3,2}
# print(57 in s)
# print(2 in s2)
# print(s.union(s2))
'''Dictionary'''
# x = {'key' : 4, 'harsh': 'pizza', 'Keshav': 'burger'}
# x['key2'] = 5
# print(x)
# print('key' in x)
# print(list(x.values()))
# del x['key2']
# print(x)
# for key,value in x.items():
#     print(key,value)
# for key in x:
#     print(key,x[key])
'''Comprehension'''
# x = [x for x in range(5)]
# print(x)
# y = [[0 for y in range(100)] for y in range(5)]
# print(y)
# z = [i for i in range(100) if i  % 5 ==0]
# print(z)
# alpha = tuple(i for i in range(1000) if i %13 == 0) 
# print(alpha)
# bita  =  {i for i in range(50) if i %7 ==0}
# print(bita)
'''functions'''
# def foo(x,y):
#     print('run',x,y)
#     return x/y,x*y
# print(foo(5,6))
''' Unpack operator and*args and **kwargs'''
# def func(x):
#     def func2():
#         print(x)
#     return func2
# x = func(3)
# x()

# def func(*args, **kwargs):
#     print(args,kwargs)
# func(1,2,3,4,5,one=3,two=9)
# x = [1,23,3434,5333424]
# print(*x)
'''*args and **kwargs is basically used for passing unlimited arguments in a function'''

'''Scope and Globals'''
# x = 'tim'
# def func(name):
#     global x
#     x = name

# print(x)
# func('changd')
# print(x)

'''Exception Handling'''
# try:
#     x =  7/0
# except Exception as e:
#     print(e)
# finally:
#     print('finally')
'''Lambda Functions'''
# x = lambda x,y: x+y
# print(x(2,35))
'''Map and Filter'''
# l1 = [1,3,4,5,6,6,7,8,8]
# mp = map(lambda i : i+2,l1)
# mp1 = filter(lambda i : i%2==0,l1)
# print(list(mp1))
# print(list(mp)) 
'''f strings'''
# harsh = 17
# x = f'hello{6+8} {harsh}'
# print(x)