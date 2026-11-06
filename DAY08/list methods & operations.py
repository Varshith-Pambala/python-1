Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
##removing in list
l= [23,44,55,663,4,54,24,,5,7,7,66]
SyntaxError: invalid syntax
l= [23,44,55,663,4,54,24,5,7,7,66]
l.pop()
66
l
[23, 44, 55, 663, 4, 54, 24, 5, 7, 7]
l.pop()
7
l.pop(0)
23
l
[44, 55, 663, 4, 54, 24, 5, 7]
l.pop(4)
54
l
[44, 55, 663, 4, 24, 5, 7]
l.remove(663)
l
[44, 55, 4, 24, 5, 7]
del l[55]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    del l[55]
IndexError: list assignment index out of range
del l[1]
l
[44, 4, 24, 5, 7]
#pop remove del
l= [23,44,55,663,4,54,24,5,7,7,66]
l.count(7)
2
l.index(55)
2
sorted(l)
[4, 5, 7, 7, 23, 24, 44, 54, 55, 66, 663]
l.sort(l)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    l.sort(l)
TypeError: sort() takes no positional arguments
l.sort()
l
[4, 5, 7, 7, 23, 24, 44, 54, 55, 66, 663]
l.reverse()
l
[663, 66, 55, 54, 44, 24, 23, 7, 7, 5, 4]
l=sort(reverse=True)
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    l=sort(reverse=True)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
l.sort(reverse=True)
l
[663, 66, 55, 54, 44, 24, 23, 7, 7, 5, 4]
a=[1,2]
c=a
c
[1, 2]
a is c
True
c is a
True
c.appenda(3)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    c.appenda(3)
AttributeError: 'list' object has no attribute 'appenda'. Did you mean '.append' instead of '.appenda'?
c.append(3)
c
[1, 2, 3]
c.extend(2)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    c.extend(2)
TypeError: 'int' object is not iterable
a
[1, 2, 3]
b=a.copy()
b
[1, 2, 3]
b.append(12)
B
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    B
NameError: name 'B' is not defined. Did you mean: 'b'?
b
[1, 2, 3, 12]
##any alll
any(l)
True
all(l)
True
l=[4, 5, 7, 7, 23, 24, 44, 54, 55, 66, 663,0]
l
[4, 5, 7, 7, 23, 24, 44, 54, 55, 66, 663, 0]
any(l)
True
all(1)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    all(1)
TypeError: 'int' object is not iterable
>>> all(l)
False
>>> any(-1)
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    any(-1)
TypeError: 'int' object is not iterable
>>> any(l)
True
>>> k=[0,0.0,'']
>>> any(k)
False
>>> all(l)
False
>>> k=[0,0.0,'',1]
>>> k
[0, 0.0, '', 1]
>>> any(k)
True
>>> all(k)
False
>>> k.append(3)
>>> k
[0, 0.0, '', 1, 3]
