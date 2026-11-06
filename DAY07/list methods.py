Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
##string checking(testing) method
s='Python programing'
s.startswith('P')
True
s.startswith('p')
False
s.endswith('ing')
True
s.endswit('img')
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    s.endswit('img')
AttributeError: 'str' object has no attribute 'endswit'. Did you mean '.endswith' instead of '.endswit'?
s.endswith('img')
False
's'islower()
SyntaxError: invalid syntax
's'.islower()
True
'M'.isupper()
True
'm'.islower()
True
'varshith'.isalpha()
True
'varshith2004'.isalpha()
False
'varshith2004'.isalnum()
True
'varshith@2004'.isalnum()
False
' '.isspace()
True
' '.isalpha()
False
'varshith'.isidentifier()
True
'varshith15'.isalnum()
True
'varshith15'.isaplha()
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    'varshith15'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean '.isalpha' instead of '.isaplha'?
'varshith15'.isaplha()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    'varshith15'.isaplha()
AttributeError: 'str' object has no attribute 'isaplha'. Did you mean '.isalpha' instead of '.isaplha'?
##isdecimal,isdigit,isnumeric
'123345'.isdecimal()
True
'98'.isdigit()
True
'0987'.isnumeric()
True
'1234a'.isdecimal()
False
##replace&modify
##splitmethod,join&particition
'abc'
'abc'
'abcd'
'abcd'

'abcd'.split()
['abcd']
'a b c d'.split()
['a', 'b', 'c', 'd']
'a b c d'.split('-')
['a b c d']
'a-b-c-d'.split('-')
['a', 'b', 'c', 'd']
'a b c d'.split('_')
['a b c d']
'a b c d'.split('-',2)
['a b c d']
'a-b-c-d'.split('-',2)
['a', 'b', 'c-d']
'a-b-c-d-e-d-a'.split('_',4)
['a-b-c-d-e-d-a']
'a-b-c-d-e-f-g'.split('_',4)
['a-b-c-d-e-f-g']
'a-b-c-d-e-f-g'.split('_',2)
['a-b-c-d-e-f-g']
'a b c d e f g'.split('',2)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    'a b c d e f g'.split('',2)
ValueError: empty separator
'a-b-c-d-e-f-g'.split('-',2)
['a', 'b', 'c-d-e-f-g']
'a b c d e'
'a b c d e'
s.splitlines()
['Python programing']
'varshith praveen codegnan'
'varshith praveen codegnan'
s.splitlines()
['Python programing']
s='varshith praveen codegnan'
s.splitlines()
['varshith praveen codegnan']
s='varshithpraveencodegnan'
s.splitlines()
['varshithpraveencodegnan']
s.splitlines(' ')
['varshithpraveencodegnan']
s='varshith,praveen,codegnan'
s.splitlines()
['varshith,praveen,codegnan']
s.splitlines(' ')

['varshith,praveen,codegnan']
'_'.join(l)
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    '_'.join(l)
NameError: name 'l' is not defined
'_'.join(s)
'v_a_r_s_h_i_t_h_,_p_r_a_v_e_e_n_,_c_o_d_e_g_n_a_n'
s='varshith praveen codegnan'
s
'varshith praveen codegnan'
'_'.join(s)
'v_a_r_s_h_i_t_h_ _p_r_a_v_e_e_n_ _c_o_d_e_g_n_a_n'
'abcd'
'abcd'
'python.py'.partion('.')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    'python.py'.partion('.')
AttributeError: 'str' object has no attribute 'partion'. Did you mean '.partition' instead of '.partion'?
'python.py'.partition('.')
('python', '.', 'py')
s='a','b','c','d'
s
('a', 'b', 'c', 'd')
s.partition()
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    s.partition()
AttributeError: 'tuple' object has no attribute 'partition'
s.partition('b')
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    s.partition('b')
AttributeError: 'tuple' object has no attribute 'partition'
s
('a', 'b', 'c', 'd')
s.partition('b'')
            
SyntaxError: unterminated string literal (detected at line 1)
s.partition('b')

Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    s.partition('b')
AttributeError: 'tuple' object has no attribute 'partition'
s.partition(',')
            
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    s.partition(',')
AttributeError: 'tuple' object has no attribute 'partition'
s
            
('a', 'b', 'c', 'd')
s='python.py'
            
s
            
'python.py'
'pyt.hon.py'.partition('.')
            
('pyt', '.', 'hon.py')
s='hello'
            
s.encode()
            
b'hello'

t="hello"
            
s.encode🙂🙂🙂
            
SyntaxError: invalid character '🙂' (U+1F642)
t='hello🙂'
            
s.encode()
            
b'hello'
##about list
            
##about list
            
l=[]
            
l
            
[]
l=[1,2,3,4]
            
l=list()
            
l=[1,2,3,4)
            
SyntaxError: closing parenthesis ')' does not match opening parenthesis '['
l=[1,2,3,4]
            
l=lits([1,2,3,4])
            
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    l=lits([1,2,3,4])
NameError: name 'lits' is not defined
l=list([1,2,3,4])
            
type(l)
            
<class 'list'>
##mut ord dup het dyn
            
l
            
[1, 2, 3, 4]
l=[1,2,3,4,5,6]
            
l
            
[1, 2, 3, 4, 5, 6]
l=[22,22,33,22,22,33]
            
l
            
[22, 22, 33, 22, 22, 33]
l=[1,1,1,1,1,1]
            
l
            
[1, 1, 1, 1, 1, 1]

l
            
[1, 1, 1, 1, 1, 1]
l
            
[1, 1, 1, 1, 1, 1]
l=(1,12.2,12+2j,'str',[1,2],(1,2),{1:2},False,None)
            
l
            
(1, 12.2, (12+2j), 'str', [1, 2], (1, 2), {1: 2}, False, None)
##cancatination,repeation,indexing,slicing,membership
            
[1,2,3]+[4,5,6]
            
[1, 2, 3, 4, 5, 6]
[1,2,3]*[4,5,6]
            
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    [1,2,3]*[4,5,6]
TypeError: can't multiply sequence by non-int of type 'list'
[1,2,3]*3
            
[1, 2, 3, 1, 2, 3, 1, 2, 3]
l=["python","java","c","flask","fastapi","mysql","aws"]
            
l=[0]
            

l
            
[0]
l=["python","java","c","flask","fastapi","mysql","aws"]
l[0]
            
SyntaxError: multiple statements found while compiling a single statement
l=["python","java","c","flask","fastapi","mysql","aws"]
            
l[0]
            
'python'
l[5]
            
'mysql'
l[:3]
            
['python', 'java', 'c']
1[:2]
            
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    1[:2]
TypeError: 'int' object is not subscriptable
l[:2]
            
['python', 'java']
l[-3:]
            
['fastapi', 'mysql', 'aws']
l
            
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
l[1:4]
            
['java', 'c', 'flask']
l[:-1:-4]
            
[]
l[:-1:-2]
            
[]
'python' in l
            
True
len(1)
            
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    len(1)
TypeError: object of type 'int' has no len()
len(l)
            
7
sorted(1)
            
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    sorted(1)
TypeError: 'int' object is not iterable
sorted(l)
            
['aws', 'c', 'fastapi', 'flask', 'java', 'mysql', 'python']
max(l)
            
'python'
min(l)
            
'aws'
l
            
['python', 'java', 'c', 'flask', 'fastapi', 'mysql', 'aws']
id(1)
            
140705821058320
l[1]
            
'java'
l[1]='html'
            
l
            
['python', 'html', 'c', 'flask', 'fastapi', 'mysql', 'aws']
id(1)
            
140705821058320
l[2]='c++'
            
l
            
['python', 'html', 'c++', 'flask', 'fastapi', 'mysql', 'aws']
l.append(1,2,3)
            
Traceback (most recent call last):
  File "<pyshell#143>", line 1, in <module>
    l.append(1,2,3)
TypeError: list.append() takes exactly one argument (3 given)
l.append(123)
            
l
            
['python', 'html', 'c++', 'flask', 'fastapi', 'mysql', 'aws', 123]
l.append(1 2 3)
            
SyntaxError: invalid syntax. Perhaps you forgot a comma?
l.append(1, 2, 3)
            
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    l.append(1, 2, 3)
TypeError: list.append() takes exactly one argument (3 given)
KeyboardInterrupt
KeyboardInterrupt
l.append('1 2 3')
...             
>>> l
...             
['python', 'html', 'c++', 'flask', 'fastapi', 'mysql', 'aws', 123, '1 2 3']
>>> l.extend('abcd')
...             
>>> l
...             
['python', 'html', 'c++', 'flask', 'fastapi', 'mysql', 'aws', 123, '1 2 3', 'a', 'b', 'c', 'd']
>>> l.insert('varshith')
...             
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    l.insert('varshith')
TypeError: insert expected 2 arguments, got 1
>>> l.insert('varshith raju')
...             
Traceback (most recent call last):
  File "<pyshell#153>", line 1, in <module>
    l.insert('varshith raju')
TypeError: insert expected 2 arguments, got 1
l.insert('varshith', 'raju')
            
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    l.insert('varshith', 'raju')
TypeError: 'str' object cannot be interpreted as an integer
l.insert(l,'varshith', 'raju')
            
Traceback (most recent call last):
  File "<pyshell#155>", line 1, in <module>
    l.insert(l,'varshith', 'raju')
TypeError: insert expected 2 arguments, got 3
l.insert(l,'varshith')
            
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    l.insert(l,'varshith')
TypeError: 'list' object cannot be interpreted as an integer
l.insert(2,'vashthith')
            
l
            
['python', 'html', 'vashthith', 'c++', 'flask', 'fastapi', 'mysql', 'aws', 123, '1 2 3', 'a', 'b', 'c', 'd']
id(l)
            
2372036512512
