Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s='python'
s
'python'
type(s)
<class 'str'>
p=''
p
''
type(p)
<class 'str'>
t='programming'
s+t
'pythonprogramming'
##it is a concating
t*3
'programmingprogrammingprogramming'
##it is a muliple by given by any number
s*7
'pythonpythonpythonpythonpythonpythonpython'
s*7
'pythonpythonpythonpythonpythonpythonpython'
s
'python'
'*'*23
'***********************'
##if we give any value it will be give the multiple by given number
s*7
'pythonpythonpythonpythonpythonpythonpython'
##indexing
s='python java flask fastapi'
a
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a
NameError: name 'a' is not defined
s
'python java flask fastapi'
s[0]
'p'
s[12]
'f'
s[22]
'a'
s[-15]
'a'
##slicing
S
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    S
NameError: name 'S' is not defined. Did you mean: 's'?
S
S='python java flask mysql fastapi'
s
'python java flask fastapi'
type(s)
<class 'str'>
s=[0:6]
SyntaxError: invalid syntax
s[0:6]
'python'
s[0:6:1]
'python'
s[7:10:1]
'jav'
s[7:11:1]
'java'
s
'python java flask fastapi'
s[:6]
'python'
s[11]
' '
s[10]
'a'
s[:11]
'python java'
s[7:11]
'java'
s[12;
  
SyntaxError: invalid syntax
s[12:17]
  
'flask'
s[24:]
  
'i'
s
  
'python java flask fastapi'
s[24:]
  
'i'
s[23:]
  
'pi'
s[18:]
  
'fastapi'
s[::-1]
  
'ipatsaf ksalf avaj nohtyp'
s[-7:]
  
'fastapi'
s[-13:]
  
'flask fastapi'
s[-13:-9:]
  
'flas'
s[-13:-10:]
  
'fla'
KeyboardInterrupt
s[-13:-8:]
  
'flask'
s[5::-1]
  
'nohtyp'
s
  
'python java flask fastapi'
##membership operations
  

s
  
'python java flask fastapi'
"java" in s
  
True
'python' is not ins
  
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    'python' is not ins
NameError: name 'ins' is not defined. Did you mean: 'int'?
'python' is not in s
  
SyntaxError: invalid syntax
'python' is not in s
  
SyntaxError: invalid syntax
'python' is not in s
  
SyntaxError: invalid syntax
s
  
'python java flask fastapi'
'python' not in s
  
False
s
  
'python java flask fastapi'
len(s)
  
25
s='varshith'
  
s
  
'varshith'
len(s)
  
8
s='varshith codegnan'
  
s
  
'varshith codegnan'
len(s)
  
17
ord(v)
  
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    ord(v)
NameError: name 'v' is not defined
ord('v')
  
118
ord('D')
  
68
ord('d')
  
100
ord(')
    
SyntaxError: unterminated string literal (detected at line 1)
ord('')
    
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    ord('')
TypeError: ord() expected a character, but string of length 0 found
ord(' ')
    
32
chr(v)
    
Traceback (most recent call last):
  File "<pyshell#81>", line 1, in <module>
    chr(v)
NameError: name 'v' is not defined
chr('100')
    
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    chr('100')
TypeError: 'str' object cannot be interpreted as an integer
chr(100)
    
'd'
chr(68)
    
'D'
ord('varshith')
    
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    ord('varshith')
TypeError: ord() expected a character, but string of length 8 found
ord('Q')
    
81
max(s)
    
'v'
max(v)
    
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    max(v)
NameError: name 'v' is not defined
max(d)
    
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    max(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
max(h)
    
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    max(h)
NameError: name 'h' is not defined
sorted(d)
    
Traceback (most recent call last):
  File "<pyshell#91>", line 1, in <module>
    sorted(d)
NameError: name 'd' is not defined. Did you mean: 'id'?
sorted(s)
    
[' ', 'a', 'a', 'c', 'd', 'e', 'g', 'h', 'h', 'i', 'n', 'n', 'o', 'r', 's', 't', 'v']
s
    
'varshith codegnan'
s= 'python java flask mysql fastapi'
    
s
    
'python java flask mysql fastapi'
s.higher()
    
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    s.higher()
AttributeError: 'str' object has no attribute 'higher'
s.tittle()
    
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    s.tittle()
AttributeError: 'str' object has no attribute 'tittle'. Did you mean '.title' instead of '.tittle'?
s
    
'python java flask mysql fastapi'
s.title()
    
'Python Java Flask Mysql Fastapi'
s.upper()
    
'PYTHON JAVA FLASK MYSQL FASTAPI'
s.lower
    
<built-in method lower of str object at 0x00000211EEB0CDA0>
s.lower()
    
'python java flask mysql fastapi'
s.capitliaze()
    
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    s.capitliaze()
AttributeError: 'str' object has no attribute 'capitliaze'. Did you mean '.capitalize' instead of '.capitliaze'?
s.capitalize()
    
'Python java flask mysql fastapi'
s.title()
    
'Python Java Flask Mysql Fastapi'
"STRASEMALAGAANGSTTROMom cafe".casefold()
    
'strasemalagaangsttromom cafe'
s.capitalize()
    
'Python java flask mysql fastapi'
s.casefold()
    
'python java flask mysql fastapi'
s='python'
    
s.center(40,'-')
    
'-----------------python-----------------'
s.center(40,' ')
    
'                 python                 '
s.ljust(111,' ')
    
'python                                                                                                         '
s.rjust(111,' ')
    
'                                                                                                         python'
s.ljust(80,' ')
    
'python                                                                          '
s.rjust(74,' ')
    
'                                                                    python'
s.rjust(71,'~')
    
'~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~python'
s.rjust(8.'praveen')
    
SyntaxError: invalid syntax. Perhaps you forgot a comma?
s.rjust(8,'praveen')
    
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    s.rjust(8,'praveen')
TypeError: The fill character must be exactly one character long
s.rjust(8,'p')
    
'pppython'
#string formating method
    
'998877'.zfill(10)
    
'0000998877'
'jdoj'.zfill(11)
    
'0000000jdoj'
s
    
'python'
s.find()
    
Traceback (most recent call last):
  File "<pyshell#124>", line 1, in <module>
    s.find()
TypeError: find expected at least 1 argument, got 0
s.find('y')
    
1
s.find('z')
    
-1
s.find('a')
    
-1
s='python java flask fastapi'


s
    
'python java flask fastapi'
s.find(a)
    
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    s.find(a)
NameError: name 'a' is not defined
s,find('a')
    
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    s,find('a')
NameError: name 'find' is not defined
s.find('s')
    
15
s.rfind('s')
    
20
s.find('t')
    
2
s.rfind('t')
    
21
s
    
'python java flask fastapi'
s.index('j')
    
7
s.index('t')
    
2
s.rindex('t')
    
21
s.index('z')
    
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    s.index('z')
ValueError: substring not found
s
    
'python java flask fastapi'
s.count('a')
    
5
s.rcount('a')
    
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    s.rcount('a')
AttributeError: 'str' object has no attribute 'rcount'. Did you mean '.count' instead of '.rcount'?
s= '     code       gnan     '
    
s.strip()
    
'code       gnan'
s.lstrip()
    
'code       gnan     '
s.rstrip()
    
'     code       gnan'
s
    
'     code       gnan     '
s='python java flask fastapi'
    
s
    
'python java flask fastapi'
s.replace('a','*')
    
'python j*v* fl*sk f*st*pi'
s.replace('p','@')
    
'@ython java flask fasta@i'
s
    
'python java flask fastapi'
s.maketrans('pslsi','12754
            
SyntaxError: unterminated string literal (detected at line 1)
s.maketrans('pslsi','12754')
            
{112: 49, 115: 53, 108: 55, 105: 52}
s.maketrans('psvsi','12754')
            
{112: 49, 115: 53, 118: 55, 105: 52}
ord(v)
            
Traceback (most recent call last):
  File "<pyshell#159>", line 1, in <module>
    ord(v)
NameError: name 'v' is not defined
>>> ord('v')
...             
118
>>> ord('p')
...             
112
>>> ord('s')
...             
115
>>> ord('1')
...             
49
>>> s.translate(s.maketrans('psvsi','12754'))
...             
'1ython ja7a fla5k fa5ta14'
>>> s.translate(s.maketrans('aeiou','*****'))
...             
'pyth*n j*v* fl*sk f*st*p*'
