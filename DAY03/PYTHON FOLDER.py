Python 3.9.13 (tags/v3.9.13:6de2ca5, May 17 2022, 16:36:42) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Welcome to my world")
Welcome to my world
>>> playing = input("Do you want to play this game? ")
Do you want to play this game? yes
>>> if playing != "Yes";
SyntaxError: invalid syntax
>>> a = 2
>>> type(a)
<class 'int'>
>>> b = 2.12
>>> type(b)
<class 'float'>
>>> c = 2+2j
>>> type(c)
<class 'complex'>
>>> b =[2,3,1,3,4]
>>> type(b)
<class 'list'>
>>> b.append(12)
>>> b
[2, 3, 1, 3, 4, 12]
>>> b.pop(3)
3
>>> b
[2, 3, 1, 4, 12]
>>> id(b)
2498825871872
>>> n = {324,13123,324,1,3,1,34,1}
>>> n'
SyntaxError: EOL while scanning string literal
>>> n
{1, 34, 3, 324, 13123}
>>> type(n)
<class 'set'>
>>> 