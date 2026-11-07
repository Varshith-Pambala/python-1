#1 reverse a string

name = "varshith"
print(name[::-1])

#2check if a string is palindrome
#compare it is reverse

word = input("enter the word: ")
print(word == word[::-1])

num = input("enter the number:")
print(num == num[::-1])

##factorial of a number
n = 5 
fact = 1 
for i in range(1, n+1): 
    fact *= i 
print(fact)

num = int(input("entrer the number: "))
fact = 1
i = 1

while i <= num:
    fact = fact*1
    i=i+1
    print("factorial is:", fact)

n = 6
fact = 1
for i in range(1,n+1):
    fact *=1
print(fact)

n = 5
fact = 1
i=1
for i in range (1,n+1):
    fact *=i
    print("factor is",fact)
    