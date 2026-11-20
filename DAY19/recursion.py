#def display(n):
#    if n>10:
#        return

#    print(n)
#    display(n+1)

#display(1)

#def display(n):
#    if n ==len(s):
#        print()
 #       return
 #   print(s[n],end=" ")
#    display(n+1)
#    print(s[n],end=" ")

#s= "python progtraming"
#display(s)

'''

def display(n):
    if n==len(s):
        print()
        return
    print(s[0])
    print(s[0:1])
    print(s[0:2])
    print(s[0:3])
    print(s[0:4])
    print(s[0:5])
    print(s[0:6])
    display(n+1)

s= "python"
display(0)

'''


'''''
def display(n):
    if n==len(s):
        print()
        return
    print(s[:n+1])
    display(n+1)


s="pyrhon"
display(0)

'''
'''''
def display(n,w):
    if n>len(s)-w:
        print()
        return()
    print(s[n:n+w])
    display(n+1,w)

s="codegnan"
display(0,4)
'''
''''
def display(n):
    if n<1:
        return 0
    return n+display(n-1)

print(display(10))

'''

''''
def factorial(n):
    if n<1:
        return 1
    return n* factorial(n-1)

print(factorial(5))
'''

'''''
def sumfirst(n):
    if n == len(l):
        return 0
    return l[n] + sumfirst(n+1)

l=[11,2234,55,754,345,7544,23,454,]
print(sumfirst(6))
'''
'''''''''
def display(n):
    if n>len(s):
        print()
        return()
    print(s[:n+1])
    display(n+1)

s="pythone"
display(0)

'''''

R