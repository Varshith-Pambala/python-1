#def numbers():
#    for i in range(1,11):
#        print(i)


#numbers()

#def factors(n):
#    c=0
#    for i in range(1,n+1):
#        if n%i==0:
#           c+=1
#    if c>2:
#        print("Not a prime number")
#    else:
#        print("Prime numbers")
#factors(int(input("Enter the nmumber to check it is prime number or not: ")))

#def isprime(n):
#    for i in range(2,n//2+1):
#        if n%i==0:
#            return"Not a prime number"
#    return "prime number"
#print(isprime(int(input('Enter the numbrer: ' ))))

#def sum_digits(n):
#    if n == 0:
#        return 0

#    return (n % 10) + sum_digits(n // 10)

#print(sum_digits(int(input('Enter the number: '))))

#def sumofdigits(n):
#   sum = 0
#    while n>0:
#        sum+= n%10
#        n//=10

#    return sum

#print(sumofdigits(int(input('Enter the number: '))))   


#def rev(n):
#    sum =0
#    while n>0:
#        sum = (sum*10) + n%10
#       n //=10
#    return sum
#print(rev(int(input("Enter the number to reverse: "))))

# ** POSTIONAL AURGEMENTS***
#def display(name,email,password):
#    print("name: ",name)
#    print("email: ",email)
#    print("password: ",password)

#display("praveen","praveen@gmail.com","praveen@123")

#**KEY MAPPING***

#def display(name,email,password):
#    print("name: ",name)
#    print("email: ",email)
#  print("password: ",password)

#display(name="praveen",email="praveen@gmail.com",password="praveen@123")
#display(email="praveen@gmail.com",name='praveen',password="praveen@123")

#*** default aurgements***
#def display(name,email,password,phonenumber=None):
#    print("name: ",name)
#    print("email: ",email)
#    print("password: ",password)
#    print("phonenumber: ",phonenumber)

#display("praveen","praveen@gmail.com","praveen123","9858294824")
#display("praveen","praveen@gmail.com","praveen123")

#def display(*n):
#    print(n)

#display(1,2,3,4)
#display(1,2,3,4,5,6,7,8,9)
#display(2,3,4,5,6,7)

#def display(**n):
#    print(n)

#display(n1=1,n2=2,n3=3,n4=4)
#display(n1=1,n2=2,n3=3,n4=4,n5=5,n6=6,n67=7,n8=8,n9=9)
#display(n1=1,n2=2,n3=3,n4=4,n5=5,n6=6,n67=7)

def highestmark(data):
    max=0
    res = ''
    for i in data:
        if data[i]>max:
            max = data[i]
            res = i
    print(f"Highest marks {res}:{max}")



data={}

for i in range(3):
    name = input("Enter the name of the student: ")
    marks = input("Enter the marks: ")
    data[name]=marks

highestmark(data)
#lowestmarks(data)