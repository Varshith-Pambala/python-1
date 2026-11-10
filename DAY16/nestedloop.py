from curses import OK


for i in range(3):
    for j in range(5):
        print(j)

for i in range(5):
    print()

for row in range(3):
    for col in range(5):
        print(col,end='')
        print()
####
for row in range(3):
    for col in range(5):
        print(1,end=' ')
    print()

for row in range(5):
    for col in range(5):
        if row %2== 0:
            print(1,end=' ')
        else:
            print(0,end=' ')
        print()

    
for row in range(5):
    for col in range(5):
        print(int(row+col) %2==0,end=' ')
        print()

for row in range(5):

    for col in range(5):
        print(col%2,end=' ')
print()


