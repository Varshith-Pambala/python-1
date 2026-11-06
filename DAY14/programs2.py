products ={
    'sugar':40,
    'salt':30,
    'bread':50,
    'butter':120,
    'coke':70,
    'chips':50,

}

#display menu
print("WELCOME TO DMART STORE".center(50,'-'))
print("Product Name","price","quantity")
for i in products:
    print(i.ljust(6,' '),':',products[i])

carts= {}
while True:
    cart= input("enter the product name(exit): ").lower()
    if cart =='exit':
        break
    qua= int(input("enter the quantity: "))
    carts[cart]=qua

    print('bill'.center(50,'-'))
    print('product Namre |quantity | price ')
    bill=0
    for i in carts:
        print(i.ljust(12,' 'str(carts[i]),ljust(6," "),products[i])
        bill += carts[i]*products[i]

    print(f"total bill: {bill}")

print("thank you for shopping"))