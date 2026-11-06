Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> ##dictinory
>>> d={}
>>> d={1:2,3:4}
>>> d
{1: 2, 3: 4}
>>> type(d)
<class 'dict'>
>>> #mut ord het uk dyn
>>> d
{1: 2, 3: 4}
>>> d[1]="int"
>>> d
{1: 'int', 3: 4}
>>> d[1.1]='float'
>>> d
{1: 'int', 3: 4, 1.1: 'float'}
>>> d[1+1j]='com'
>>> d
{1: 'int', 3: 4, 1.1: 'float', (1+1j): 'com'}
>>> d[False]='bool'
>>> d
{1: 'int', 3: 4, 1.1: 'float', (1+1j): 'com', False: 'bool'}
>>> d[(1,2,3)]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    d[(1,2,3)]
KeyError: (1, 2, 3)
d[(1,2,3)]'tuple'
SyntaxError: invalid syntax

SyntaxError: invalid syntax
SyntaxError: invalid syntax


d[(1,2,3)]='tuple'
d
{1: 'int', 3: 4, 1.1: 'float', (1+1j): 'com', False: 'bool', (1, 2, 3): 'tuple'}
d[[1,2,3]]='tuple'
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    d[[1,2,3]]='tuple'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d[[1,2,3]]='list'
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    d[[1,2,3]]='list'
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
d{1:1,2:2,3:2}]='tuple'
SyntaxError: unmatched ']'
d[{1:1,2:2,3:2}]='tuple'
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    d[{1:1,2:2,3:2}]='tuple'
TypeError: cannot use 'dict' as a dict key (unhashable type: 'dict')
d.clear
<built-in method clear of dict object at 0x000002B663B91C00>
sort(d)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    sort(d)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
sorted(d)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    sorted(d)
TypeError: '<' not supported between instances of 'complex' and 'float'
d
{1: 'int', 3: 4, 1.1: 'float', (1+1j): 'com', False: 'bool', (1, 2, 3): 'tuple'}
a.append(1.1)
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    a.append(1.1)
NameError: name 'a' is not defined
d.append(1.1)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d.append(1.1)
AttributeError: 'dict' object has no attribute 'append'
d
{1: 'int', 3: 4, 1.1: 'float', (1+1j): 'com', False: 'bool', (1, 2, 3): 'tuple'}
d.clear()
d
{}
d[1]=1
d[2]=12.2
d[3]=1+3j
d[4]='varshith'
d[5]=[list]
d[6]=(1,9)
d[5]=[1,2,3]
D(7)={1,2}
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
d(7)={1,2}
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
d[9]=False
d(7)={1,2}
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
d(8)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    d(8)
TypeError: 'dict' object is not callable
=
d(8)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    d(8)
TypeError: 'dict' object is not callable
d(8)={1:2,3:3}
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: [1, 2, 3], 6: (1, 9), 9: False}
d[2]
12.2
d[3]
(1+3j)
d[4]
'varshith'
d.get(6)
(1, 9)
d.get(9)
False
d.get(1)
1
d.get(10)
d.get(7)
d.get(9)
False
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: [1, 2, 3], 6: (1, 9), 9: False}
'varshith' in d
False
'varshith' not in d
True
[1,2] in d
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    [1,2] in d
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')
{1,2} in d
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    {1,2} in d
TypeError: cannot use 'set' as a dict key (unhashable type: 'set')
(1,2,3) in d
False
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: [1, 2, 3], 6: (1, 9), 9: False}
d[8]={200}
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: [1, 2, 3], 6: (1, 9), 9: False, 8: {200}}
sort(d)
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    sort(d)
NameError: name 'sort' is not defined. Did you mean: 'sorted'?
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: [1, 2, 3], 6: (1, 9), 9: False, 8: {200}}
d[8]='dict'
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: [1, 2, 3], 6: (1, 9), 9: False, 8: 'dict'}
d[5]=5
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: 5, 6: (1, 9), 9: False, 8: 'dict'}
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: 5, 6: (1, 9), 9: False, 8: 'dict'}
d[13]=100
d[14]=200
d[15]=300
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: 5, 6: (1, 9), 9: False, 8: 'dict', 13: 100, 14: 200, 15: 300}
d.update({16:400,17:500})
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: 5, 6: (1, 9), 9: False, 8: 'dict', 13: 100, 14: 200, 15: 300, 16: 400, 17: 500}
#update and modicication done
##now delete
d.pop()
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
d.popitem()
(17, 500)
d.pop(8)
'dict'
d.pop()
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    d.pop()
TypeError: pop expected at least 1 argument, got 0
d.popitem()
(16, 400)
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: 5, 6: (1, 9), 9: False, 13: 100, 14: 200, 15: 300}
del d[5]
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 6: (1, 9), 9: False, 13: 100, 14: 200, 15: 300}
del d[15r]
SyntaxError: invalid decimal literal
del d[15]
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 6: (1, 9), 9: False, 13: 100, 14: 200}
d. clear()
d
{}
#methods
d.keys()
dict_keys([])
d={1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: 5, 6: (1, 9), 9: False, 8: 'dict', 13: 100, 14: 200, 15: 300, 16: 400, 17: 500}
d
{1: 1, 2: 12.2, 3: (1+3j), 4: 'varshith', 5: 5, 6: (1, 9), 9: False, 8: 'dict', 13: 100, 14: 200, 15: 300, 16: 400, 17: 500}
d.keys()
dict_keys([1, 2, 3, 4, 5, 6, 9, 8, 13, 14, 15, 16, 17])
d.values()
dict_values([1, 12.2, (1+3j), 'varshith', 5, (1, 9), False, 'dict', 100, 200, 300, 400, 500])
d.items()
dict_items([(1, 1), (2, 12.2), (3, (1+3j)), (4, 'varshith'), (5, 5), (6, (1, 9)), (9, False), (8, 'dict'), (13, 100), (14, 200), (15, 300), (16, 400), (17, 500)])
len(d)
13
max(d)
17
min(d)
1
sorted(d)
[1, 2, 3, 4, 5, 6, 8, 9, 13, 14, 15, 16, 17]
max(d)
17
min(d)
1
d.clear()
d
{}
a={1:1,2:3}
b=a
a
{1: 1, 2: 3}
b
{1: 1, 2: 3}
sorted(a)
[1, 2]
max(a)
2
min(a)
1
a.append(1:2)
SyntaxError: invalid syntax
a.appem({1:2})
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    a.appem({1:2})
AttributeError: 'dict' object has no attribute 'appem'
a.append({1:2})
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    a.append({1:2})
AttributeError: 'dict' object has no attribute 'append'
a.update({1:5})
a
{1: 5, 2: 3}
a
{1: 5, 2: 3}
d=dict.fromkeys(['a','b','c','d','e'],0)
d
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0}
d.setdefault('b')
0
d.setdefault(f')
             
SyntaxError: unterminated f-string literal (detected at line 1)
d.setdefault('f')
             
d
             
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': None}
d.setdefault('g',varshith)
             
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    d.setdefault('g',varshith)
NameError: name 'varshith' is not defined
d.setdefault('g',15)
             
15
d
             
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': None, 'g': 15}
s=frozenset({1,2,3,4,5})
             
s
             
frozenset({1, 2, 3, 4, 5})
len(s)
             
5
max(s)
             
5

min(s)
             
1
sorted(s)
             
[1, 2, 3, 4, 5]
type(s)
             
<class 'frozenset'>
