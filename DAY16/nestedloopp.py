#C=1

#for row in range(5):
#    for col in range(5):
#       print(C,end=' ')
#       C +=1
#    print()

#for row in range(5):
 #   for col in range(5):
#        print(row*col,end=' ')
#    print()
####
#for row in range(5):
#    for col in range(row+1):
#        print('*',end=' ')
#   print()

###
#n= int(input("enter the size: "))
#for row in range(n):
#    for col in range(row+1):
#       print('*',end=' ')
#    print()

####
n= int(input("enter the size: "))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()
