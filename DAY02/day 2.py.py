Python 3.15.0 (tags/v3.15.0:d220409, Oct  9 2026, 11:55:56) [MSC v.1951 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
 import keyword

           print(keyword.kwlist)
           print(len(keyword.kwlist)

SyntaxError: unexpected indent
import keyword
print(keyword.kwlist)
print(len(keyword.kwlist)
      
SyntaxError: multiple statements found while compiling a single statement
import keyword
      
print(keyword.kwlis)
      
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print(keyword.kwlis)
AttributeError: module 'keyword' has no attribute 'kwlis'. Did you mean '.kwlist' instead of '.kwlis'?
>>> print(keyword.kwlist)
...       
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> print(len(keyword.kwlist)
... 
...       a=10
...       
SyntaxError: '(' was never closed
>>> a=10
...       
>>> b=20
...       
>>> c=30
...       
>>> a=b=c=10
...       
>>> a
...       
10
>>> b
...       
10
>>> c
...       
10
>>> a,b,c=10,20,30
...       
>>> a
...       
10
>>> b
...       
20
>>> c
...       
30
