Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
================== RESTART: C:/Users/sainithin/Downloads/demo.py ==================
0
1
2
3
4
5
6
7
8
9
>>> b=5
>>> print(b)
5
>>> print('b=',b)
b= 5
>>> print('b =',b)
b = 5
>>> print(type(b))
<class 'int'>
>>> 
>>> a=10
>>> print(a)
10
>>> type(a)
<class 'int'>
>>> a='hello'
>>> print(a)
hello
>>> type(a)
<class 'str'>
>>> a=3.14
>>> type(a)
<class 'float'>
>>> a=true
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    a=true
NameError: name 'true' is not defined
>>> a=True
>>> a =[2,4,6,7,8]
>>> type(a)
<class 'list'>
>>> a(1,3,5,7)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a(1,3,5,7)
TypeError: 'list' object is not callable
>>> a=(1,3,5,7)
>>> type(a)
<class 'tuple'>
>>> 