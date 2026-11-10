pin = 1234
for i in range(5):
    epin=int(input("enter the pin: "))

    if epin == pin:
        print("login sucessful")
    else:
        print("invalid password")


## list
l= [1,4,5,7,11,43,56,78,112,5566,3338]
search = int(input("enter the number: "))
for i in range(len(l)):
    if l[i] == search:
        print(f"{search}is found in i")
    else:
        print(f"{search}not found in i")