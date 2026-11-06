Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # bit wise operator
>>> 11|15
15
>>> 11|12
15
>>> 11^12
7
>>> 5&14
4
>>> 11&12
8
>>> 11^12
7
>>> ~11
-12
>>> ~3244
-3245
>>> 432~
SyntaxError: invalid syntax
>>> 13~
SyntaxError: invalid syntax
>>> ~12
-13
>>> 2>>1
1
>>> 14>>2
3
>>> 14<<2
56
>>> 5>>1
2
\
>>> 22<<1
44
>>> a = input()
praveen
>>> type (a)
<class 'str'>
>>> a = input()
43242
>>> type(a)
<class 'str'>
>>> a
'43242'
>>> a = int(input("Enter the amount to be transfered "))
Enter the amount to be transfered 13
>>> a = int(input("Enter the amount to be transfered: "))
Enter the amount to be transfered: 243
>>> a = float(input("enter the floate value: "))
enter the floate value: 13
>>> a
13.0
>>> 13.0
13.0
>>> 
>>> --> rawr
SyntaxError: invalid syntax
>>> a= 13.0
>>> a = list(input())
123 1233 13
>>> a
['1', '2', '3', ' ', '1', '2', '3', '3', ' ', '1', '3']
>>> a = list(map(int,input().split()))
1 3 45 53 654 24 
>>> a
[1, 3, 45, 53, 654, 24]
>>> a = list(map(float,input().split()))
123.091 1213.312  1331 11433.4432
>>> a
[123.091, 1213.312, 1331.0, 11433.4432]
>>> a = tuple(map(float,input().split()))
12 313 142 414 45 13.131
>>> a
(12.0, 313.0, 142.0, 414.0, 45.0, 13.131)
>>> a,b,c = list(map(int,input().split()))
23 231 53 12 42
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a,b,c = list(map(int,input().split()))
ValueError: too many values to unpack (expected 3)
>>>  a,b,c = list(map(int,input().split()))
 
SyntaxError: unexpected indent
>>> a,b,c = list(map(int,input().split()))
12 132 123
>>> a
12
>>> b
132
>>> c
123
>>> a = eval(input())
(1,2,3,4)
>>> a
(1, 2, 3, 4)
>>> type(a)
<class 'tuple'>
>>> a = eval(input())
'praveen'
>>> a
'praveen'
>>> a = eval(input())
{1:2,2:3,3:4}
>>> a
{1: 2, 2: 3, 3: 4}
>>> type(a)
<class 'dict'>
>>> a = eval(input())
True
>>> a
True
>>> type(a)
<class 'bool'>
>>> a = eval(input())
2+3j
>>> type(a)
<class 'complex'>
>>> <class 'complex'>
SyntaxError: invalid syntax
>>> a = 10
>>> b = 12.1
>>> c = 'praveen'
>>> print(a,b,c)
10 12.1 praveen
>>> print('f a{}=a b{]=b c{}=c ')
f a{}=a b{]=b c{}=c 
>>> print('a=',a"b=",b "c=",c)
SyntaxError: invalid syntax
>>> print('a=',a'b=',b 'c=",c)

SyntaxError: invalid syntax
>>> print('a=',a 'b=',b 'c=',c)
SyntaxError: invalid syntax
>>> print('a=',a,'b=',b, 'c=",c)
      
SyntaxError: EOL while scanning string literal
>>> SyntaxError: EOL while scanning string literal
SyntaxError: invalid syntax
>>> print(f'a={a} b= {b} c={c}')
a=10 b= 12.1 c=praveen
>>> print('a=%d b=%2.f c= &s'%(a,b,c))
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    print('a=%d b=%2.f c= &s'%(a,b,c))
TypeError: not all arguments converted during string formatting
>>> print('a=%d b=%.2f c=%s' % (a,b,c))
a=10 b=12.10 c=praveen
>>> 