Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s={12,34,5,667,24,90}
s
{34, 5, 24, 90, 667, 12}
sorted(s)
[5, 12, 24, 34, 90, 667]
len(s)
6
max(s)
667
min(s)
5
sum(s)
832
any(s)
True
all(s)
True
s={12,34,5,667,24,90,0}
s
{0, 34, 5, 24, 90, 667, 12}
any(s)
True
all(s)
False
s
{0, 34, 5, 24, 90, 667, 12}
s.add(100,22,33)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s.add(100,22,33)
TypeError: set.add() takes exactly one argument (3 given)
s,add91222)
SyntaxError: unmatched ')'
s.add(122)
s
{0, 34, 5, 122, 24, 90, 667, 12}
s.update(11,223,44,)
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    s.update(11,223,44,)
TypeError: 'int' object is not iterable
s.update({11,223,44,})
s
{0, 34, 5, 90, 11, 12, 44, 24, 122, 667, 223}
sorted(s)
[0, 5, 11, 12, 24, 34, 44, 90, 122, 223, 667]
s.pop(12)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s.pop(12)
TypeError: set.pop() takes no arguments (1 given)
s.pop()
0
s.remove(11)
s
{34, 5, 90, 12, 44, 24, 122, 667, 223}
s.pop()
34
s.remove(11)
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    s.remove(11)
KeyError: 11
s.discard(11)
s
{5, 90, 12, 44, 24, 122, 667, 223}
s.discard(90)
s
{5, 12, 44, 24, 122, 667, 223}
s.clear()
>>> s
set()
>>> s
set()
>>> a={1,2,3,4,5,6}
>>> a
{1, 2, 3, 4, 5, 6}
>>> b=a
>>> a
{1, 2, 3, 4, 5, 6}
>>> b
{1, 2, 3, 4, 5, 6}
>>> c=a.copy()
>>> c
{1, 2, 3, 4, 5, 6}
>>> a.add(20)
>>> a
{1, 2, 3, 4, 5, 6, 20}
