bill = 0

while True:
    product= input("enter the product name(stop): ")
    if product == 'stop':
        print("total bill:", bill)
        break
    price= int(input("enter the price: "))
    quantity= int(input("enter the quantity: "))
    bill+= price*quantity