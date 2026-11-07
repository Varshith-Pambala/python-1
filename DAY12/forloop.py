#str list tupple set dic range
a = input("enter the word: ")
for i in a:
    if i in 'aeiouAEIOU':
        print (i)
S = [12,23,445,55,32]
for i in S:
    print(i)

a = list(map(int,input("enter the numms: ").split()))
for i in a:
    if i%2==0:
        print(i)


sumoftuple = 0 
s=tuple(map(int,input("enter the number: ").split()))
if i in s:
    sumoftuple+=1
    print("sum of tuple:", sumoftupple)

s={10,23,20,21,32,12}
if i in s:
    print(i)

max = 0
a=set(map(int,input("enter the numbers:").split()))
for i in a:
    if i>max:
        max = i
print("max of set",set)


marks={'python':90,'mysql':75,'css':90}
for i in marks:
    print(i,marks[i])

sum=0
marks={'python':90,'mysql':75,'css':90}
for i in marks:
    print("total marks", sum)

        