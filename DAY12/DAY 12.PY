'''
s = 'codegnan' 
for i in  s:
   print(i)         

   a = input("Enter the word: ")
   for i in a:
           print(i)


p= [1,45,23,53,24,64,25,87,97,97,34,65,76,87,98,99]
for i in p:
   print(i)

 a=list(map(int,input("Enter the numbers: ").split()))
for i in a:
    if i % 2 == 0:
        print((i)


sumoftuple = 0
a = tuple(map(int,input("Enter the numbers: ").split()))
for i in a:
    sumoftuple += i 
print("sum of tuple: ",sumoftuple)

'''
'''
s = [1,2,3,4,5,6,7,8,9]
for i in s:
    print(i)

max = 0
a = set(map(int,input("Enter the numbers: ").split()))
for i in a:
    if i > max:
        max = i 
print("max number of set is: ",max)
'''

'''
marks = {'python': 90, 'java': 80, 'c++': 70, 'c#': 60}
for i in marks:
    print(i, marks[i])

sum = 0
marks = {'python': 90, 'java': 80, 'c++': 70, 'c#': 60}
for i in marks:
    sum += marks[i]


print("total number of marks: ", sum)
'''
'''
for i in range (1, 11):
    print(i)   

for i in range(20, 0, -1):
    print(i)    

for i in range(2,101,2):
    print(i)


n = int(input("Enter the table no: "))

for i in range(1, 21):
    print(f"{n} * {i} = {n*i}")


c = "codegnan"

for i in range(len(c)):
    print(c[i],i,end = " ")
sum = 0
c = ["12,34,45,67,78,43,80"]
for i in range(len(c)):
    if c[i] % 2 == 0:
        sum += i     
print(sum)

for i in range(1, 11):
    if i == 5:
        break
    print(i)    
'''
for i in range(1, 11):
    pass
if True:
 pass
class booking:
    pass