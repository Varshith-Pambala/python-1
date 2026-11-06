Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = 10
>>> b = 5
>>> a + b
15
>>> a - b
5
>>> a  * b
50
>>> a / b
2.0
>>> a // b
2
>>> a % b
0
>>> a ** b
100000
>>> # + , - , * , / , // , % , **
>>> # comparison operators
>>> a = 2
>>> b = 5
>>> a < b
True
>>> a > b
False
>>> a <= b
True
>>> a > = b
SyntaxError: invalid syntax
>>> a >=
SyntaxError: invalid syntax
>>> a >= b
False
>>> a == b
False
>>> a != b
True
>>> # <,>,<=,>=,==,!=
>>> a =10
>>> b =10
>>> a<b
False
>>> a>b
False
>>> ## assignment operators
>>> c = 10
>>> c
10
>>> c += 10
>>> c
20
>>> c -= 10
>>> c
10
>>> c *= 2
>>> c
20
>>> c /= 5
>>> c
4.0
>>> c //= 5
>>> c
0.0
>>> c **= 5
>>> c
0.0
>>> 20
20

>>> 
>>> 
>>> # logical operators
>>> # and ,or,not
>>> a = 10
>>> a
10
>>> a %2 == 0 and a <11
True
>>> >>> a %2 == 0 and a <9
SyntaxError: invalid syntax
>>> a %2 == 0 and a <11
True
>>> a %2 == 0 or a <9
True
>>> not a%2 == 0
False
>>> # membership operation
>>> # in
>>> # in
\
>>> # str, set,list,tuple,dict
>>> s = 'praveen'
>>> s
'praveen'
>>> 'p' in s
True
>>> 'p' not in s
False
>>> b = [1,2,3,4,5]
>>> type(b)
<class 'list'>
>>> 3 in b
True
>>> 5 in b
True
>>> 10 in b
False
>>> 3 not in b
False
>>> g = {1,4,5,6,7}
>>> type(g)
<class 'set'>
>>> 6 in g
True
>>> 6 not in g
False
>>> v = (2,43,5,6,7)
>>> type(v)
<class 'tuple'>
>>> 43 in v
True
>>> 43 not in v
False
>>> m = {1:2,2:4,3:6,4:8}
>>> type(m)
<class 'dict'>
>>> 10 in m
False
>>> 2 in m
True
>>> 7 in m
False
>>> # identity operator
>>> # to check the memory location
>>> l = [1,2,3,4,5]
>>> m =[1,2,3,4,5]
>>> l is m
False
>>> l == m
True
>>> m =n
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    m =n
NameError: name 'n' is not defined
>>> n = m
>>> m is n
True
>>> l is not m
True
>>> id (l)
1779111817152
>>> id(m)
1779111939072
>>> id(n)
1779111939072
>>> k = 10
>>> j = 20
>>> id (K)
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    id (K)
NameError: name 'K' is not defined
>>> id(k)
1779070560848
>>> id(j)
1779070561168
>>> j = u
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    j = u
NameError: name 'u' is not defined
>>> u = j
>>> 