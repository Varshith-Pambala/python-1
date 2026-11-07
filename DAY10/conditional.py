#product = input("Enter the product name: ")
#bestseller = eval(input("Enter the status?  "))

#f bestseller:
 #   print(f"{product} is a best seller!")


#batterycharge = input("Enter the battery percentage: ")

##   print(f"Battery is low:{batterycharge},charge your phone!")

bill = int(input("enter the bill amount: "))
status = input("Is it raning: ")

if status:
    bill+=30
    print("Extra delivery charges are applied.")
print(f"final Bill amount is: {bill}")
##

batterycharge = input("enter the battery percentage: ")
status = int(input("battery percentage: "))

if status <= 20:
    print(f"battery is low,{batterycharge},pleasecharge!")

batterypercentage = int(input("enter the batterypercentage: "))
if batterypercentage == 20:
    print(f"{batterypercentage},is very low!")s