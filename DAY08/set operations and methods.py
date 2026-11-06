Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
##set operations
##unordered uni mut het dyn
s=set()
s
set()
s={1,2,3,4}
s
{1, 2, 3, 4}
type(S)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    type(S)
NameError: name 'S' is not defined. Did you mean: 's'?
Type()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    Type()
NameError: name 'Type' is not defined. Did you mean: 'type'?
type(s)
<class 'set'>
s={64,83,99,53,049,62,2,2,233,}
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
s={64,83,99,53,49,62,2,2,233,}
s
{64, 2, 99, 233, 49, 83, 53, 62}
s={1,1,1,1,1,1,}
s
{1}
s=set()|
SyntaxError: invalid syntax
s=set()
s
set()
s.add(1)
s
{1}
s.add(3)
s
{1, 3}
s={1,1,1,1,1,1,}
s
{1}
s.add(1+22j)
S
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    S
NameError: name 'S' is not defined. Did you mean: 's'?
s
{1, (1+22j)}
s.add('str')
s
{1, (1+22j), 'str'}
s
{1, (1+22j), 'str'}
s.add(False)
s
{False, 1, (1+22j), 'str'}
s.add([1,2,3])
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    s.add([1,2,3])
TypeError: cannot use 'list' as a set element (unhashable type: 'list')
s.add({1,22,3})
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    s.add({1,22,3})
TypeError: cannot use 'set' as a set element (unhashable type: 'set')
##set operations
 a{2,3,5,6}
 
SyntaxError: unexpected indent
a{2,3,5,6}
SyntaxError: invalid syntax
a={2,3,5,6}
b={8,3,4,6}
a
{2, 3, 5, 6}
b
{8, 3, 4, 6}
4 in b
True
3 in b
True
3 not in b
False
a | b
{2, 3, 4, 5, 6, 8}
a&b
{3, 6}
a
{2, 3, 5, 6}

b
{8, 3, 4, 6}
a.isdisjoint(b)
False
a={2,3,5,6}
b={2,3,5,6}
a.isdisjoint(b)
False
>>> a={2,3,5,6}
>>> b={8,3,4,6}
>>> a.isdisjoint({3,4})
False
>>> a.isdisjoint({11,33})
True
>>> a
{2, 3, 5, 6}
>>> {2}.issubset(a)
True
>>> {3}.issubset(a)
True
>>> {7}.issubset(a)
False
>>> {,1,2,3,4,5,6,7,8}.issuperset(a)
SyntaxError: invalid syntax
>>> {1,2,3,4,5,6,7,8}.issuperset(a)
True
>>> {1,4,7,8}.issuperset(a)
False
