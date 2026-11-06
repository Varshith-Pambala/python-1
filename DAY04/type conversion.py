Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a  = 10
>>> a
10
>>> float(a)
10.0
>>> complex(a)
(10+0j)
>>> str(a)
'10'
>>> list(a)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    list(a)
TypeError: 'int' object is not iterable
>>> set(a)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    set(a)
TypeError: 'int' object is not iterable
>>> tuple(a)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    tuple(a)
TypeError: 'int' object is not iterable
>>> dict(a)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    dict(a)
TypeError: 'int' object is not iterable
>>> b = 2.3
>>> b
2.3
>>> int(b)
2
>>> complex(b)
(2.3+0j)
>>> list(b)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    list(b)
TypeError: 'float' object is not iterable
>>> set(b)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    set(b)
TypeError: 'float' object is not iterable
>>> tuple(b)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    tuple(b)
TypeError: 'float' object is not iterable
>>> dict(b)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    dict(b)
TypeError: 'float' object is not iterable
>>> bool(b)
True
>>> bool(0)
False
>>> c =1+2J
>>> c
(1+2j)
>>> int(c)
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    int(c)
TypeError: can't convert complex to int
>>> float(c)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    float(c)
TypeError: can't convert complex to float
>>> str(c)
'(1+2j)'
>>> list(c)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    list(c)
TypeError: 'complex' object is not iterable
>>> set(c)
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    set(c)
TypeError: 'complex' object is not iterable
>>> tuple(c)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    tuple(c)
TypeError: 'complex' object is not iterable
>>> dict(c)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    dict(c)
TypeError: 'complex' object is not iterable
>>> bool(c)
True
>>> bool(0)
False
>>> d = 'praveen'
>>> d
'praveen'
>>> int(d)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    int(d)
ValueError: invalid literal for int() with base 10: 'praveen'
>>> float(d)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    float(d)
ValueError: could not convert string to float: 'praveen'
>>> complex(d)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    complex(d)
ValueError: complex() arg is a malformed string
>>> list(d)
['p', 'r', 'a', 'v', 'e', 'e', 'n']
>>> set(d)
{'p', 'a', 'e', 'n', 'r', 'v'}
>>> tuple(d)
('p', 'r', 'a', 'v', 'e', 'e', 'n')
>>> dict(d)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    dict(d)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> bool(d)
True
>>> d = '1234'
>>> d
'1234'
>>> int(d)
1234
>>> float(d)
1234.0
>>> complex(d)
(1234+0j)
>>> list(d)
['1', '2', '3', '4']
>>> set(d)
{'1', '2', '3', '4'}
>>> a = 34
>>> type(a)
<class 'int'>
>>> int(a)
34
>>> c = 1 + 2J
>>> c
(1+2j)
>>> type(c)
<class 'complex'>
>>> complex(c)
(1+2j)
>>> list[1,2,3,4]
list[1, 2, 3, 4]
>>> e = [1,2,3,4,5]
>>> type(e)
<class 'list'>
>>> int(e)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    int(e)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> float(e)
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    float(e)
TypeError: float() argument must be a string or a number, not 'list'
>>> compex(e)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    compex(e)
NameError: name 'compex' is not defined
>>> complex(e)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    complex(e)
TypeError: complex() first argument must be a string or a number, not 'list'
>>> str(e)
'[1, 2, 3, 4, 5]'
>>> set(e)
{1, 2, 3, 4, 5}
>>> tuple(e)
(1, 2, 3, 4, 5)
>>> dict(e)
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    dict(e)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> bool(e)
True
>>>  v = [1,2,3,4,5]
 
SyntaxError: unexpected indent
>>> v = [1,2,3,4,5,4]
>>> type(v)
<class 'list'>
>>> v = {1,2,3,4,5,5}
>>> type(v)
<class 'set'>
>>> int(v)
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    int(v)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'set'
>>> float(v)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    float(v)
TypeError: float() argument must be a string or a number, not 'set'
>>> str(v)
'{1, 2, 3, 4, 5}'
>>> complex(v)
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    complex(v)
TypeError: complex() first argument must be a string or a number, not 'set'
>>> list(v)
[1, 2, 3, 4, 5]
>>> tuple(v)
(1, 2, 3, 4, 5)
>>> bool(v)
True
>>> m = { 1:2,2:3,4:5}
>>> type(m)
<class 'dict'>
>>> int(m)
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    int(m)
TypeError: int() argument must be a string, a bytes-like object or a number, not 'dict'
>>> float(m)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    float(m)
TypeError: float() argument must be a string or a number, not 'dict'
>>> str(m)
'{1: 2, 2: 3, 4: 5}'
>>> complex(m)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    complex(m)
TypeError: complex() first argument must be a string or a number, not 'dict'
>>> list(m)
[1, 2, 4]
>>> set(m)
{1, 2, 4}
>>> ''
''
>>> 