data={

    123456:{"pin":1234,"balance":5000,"transactions":[]},
    123457:{"pin":1234,"balance":6000,"transactions":[]},
    123458:{"pin":1234,"balance":7000,"transactions":[]},
    123459:{"pin":1234,"balance":8000,"transactions":[]}
}

def login():
    global acc_num
    acc_num = int(input("Enter the acconunt number: "))
    pin = int(input("Enter the pin: "))
    if acc_num in data and data[acc_num]["pin"]==pin:
        print("login succesfully")
        return True
    else:
        print("invalid attempt")
        return False

def menu():
    print()
    print('[C]eck balance')
    print('[D]eposit')
    print('[W]ithdraw')
    print('[T]ransactions')
    print('change [P]in')
    print('[E]xit')

def checkbalance():
    print(f"Current balance is {data[acc_num]['balance']}")

def deposit():
    amount = int(input("Enter the amount: "))
    data[acc_num]["balance"]+=amount
    data[acc_num]['transactions'].amount(f'deposit:${amount}/-')
    print(f'{amount}is deposit succesfully')

def withdraw():
    amount = int(input("Enter the amount: "))
    if data[acc_num]["balance"]>=amount:
        data[acc_num]["balance"]-=amount
        data[acc_num]['transactions'].append(f'withdraw: ${amount}/-')
        print(f'{amount}is withdraw  succesfully')
    else:
        print("insufficient balance")


def transactions():
    if data[acc_num]["transaction"]:
        print("--------transaction history--------")
        for i in data[acc_num]["transaction"]:
            print(i)
    else:
        print("no transactions pending")
print()