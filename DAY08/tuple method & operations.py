Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
KeyboardInterrupt
##imm ord dul het fix
t=()
t=tuple()
t=(1,2,3)
t
(1, 2, 3)
t=tuple((1,2,3,4))
t
(1, 2, 3, 4)
type(t)
<class 'tuple'>
t
(1, 2, 3, 4)
t=(1)
t
1
type(t)
<class 'int'>
t=(1,)
t
(1,)
t=1,2,3,4
t
(1, 2, 3, 4)
type(t)
<class 'tuple'>
t=(1,1.1,1+2j,'iug',[1,2,3],{1,2,2},(1,2),{1;:},False)
SyntaxError: invalid syntax
t=(1,1.1,1+2j,'iug',[1,2,3],{1,2,2},(1,2),{1:1},False)

t
(1, 1.1, (1+2j), 'iug', [1, 2, 3], {1, 2}, (1, 2), {1: 1}, False)
type(t)
<class 'tuple'>
 ##we can change the list or anyother which are muteable not immu
a,b,c,d=t
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    a,b,c,d=t
ValueError: too many values to unpack (expected 4, got 9)
t
(1, 1.1, (1+2j), 'iug', [1, 2, 3], {1, 2}, (1, 2), {1: 1}, False)
t=(1,2,3,4)

t
t
(1, 2, 3, 4)
a,b,c,d=t
a
1
b
2
c
3
a
1
d
4
a,b,c=(1,2,3)
a
1
b
2
c
3
##it is a pack and unpack method
t=(1,1.1,1+2j,'iug',[1,2,3],{1,2,2},(1,2),{1:1},False)
t
(1, 1.1, (1+2j), 'iug', [1, 2, 3], {1, 2}, (1, 2), {1: 1}, False)
t
(1, 1.1, (1+2j), 'iug', [1, 2, 3], {1, 2}, (1, 2), {1: 1}, False)
len(t)
9
t.append[4]
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    t.append[4]
AttributeError: 'tuple' object has no attribute 'append'. Did you mean to use a 'list' object?
t[3]
'iug'
t[4].append(1)
t
(1, 1.1, (1+2j), 'iug', [1, 2, 3, 1], {1, 2}, (1, 2), {1: 1}, False)
##tuple operations
a=(1,2,3,4,5)
b=(6,7,8)
a
(1, 2, 3, 4, 5)
b
(6, 7, 8)
a+b
(1, 2, 3, 4, 5, 6, 7, 8)
a*b
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a*b
TypeError: can't multiply sequence by non-int of type 'tuple'
a*1
(1, 2, 3, 4, 5)
a*2
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
a*3
(1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5)
t
(1, 1.1, (1+2j), 'iug', [1, 2, 3, 1], {1, 2}, (1, 2), {1: 1}, False)
t[2]
(1+2j)
t[5]
{1, 2}
t[-1]
False
t[:1]
(1,)
t[-1:-2:]
()
t[-1:2]
()
t[::-1]
(False, {1: 1}, (1, 2), {1, 2}, [1, 2, 3, 1], 'iug', (1+2j), 1.1, 1)
t[::-3]
(False, {1, 2}, (1+2j))
t
(1, 1.1, (1+2j), 'iug', [1, 2, 3, 1], {1, 2}, (1, 2), {1: 1}, False)
t[::3]
(1, 'iug', (1, 2))
t[-2:]
({1: 1}, False)
1  in t
True
1,2 in t
(1, False)
false in t
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    false in t
NameError: name 'false' is not defined. Did you mean: 'False'?
False in t
True
t=(12,22,33,445,75,235,645)
t
(12, 22, 33, 445, 75, 235, 645)
len(t)
7
sorted(t)
[12, 22, 33, 75, 235, 445, 645]
sort(t)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    sort(t)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
t.sort(t)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    t.sort(t)
AttributeError: 'tuple' object has no attribute 'sort'
t.sort()
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    t.sort()
AttributeError: 'tuple' object has no attribute 'sort'
max(t)
645
min(t)
12
count(2)
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    count(2)
NameError: name 'count' is not defined. Did you mean: 'round'?
count(2)
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    count(2)
NameError: name 'count' is not defined. Did you mean: 'round'?
count(22)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    count(22)
NameError: name 'count' is not defined. Did you mean: 'round'?
round(2)
2
>>> round(3)
3
>>> t.count(2)
0
>>> t
(12, 22, 33, 445, 75, 235, 645)
>>> t.count(33)
1
>>> t.index(445)
3
>>> any(t)
True
>>> all(t)
True
>>> t=[12, 22, 33, 445, 75, 235, 645]
>>> t
[12, 22, 33, 445, 75, 235, 645]
>>> t=[12, 22, 33, 445, 75, 235, 645,0]
>>> all(t)
False
>>> t
[12, 22, 33, 445, 75, 235, 645, 0]
>>> sum(t)
1467
