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
'''''
n= int(input("enter the size: "))
for row in range(n):
    for col in range(n-row):
        print('*',end=' ')
    print()

    '''
'''''
n = int(input("enter the size: "))

for i in range(n):
    for j in range(n):
        if ((i==0 or i==n-1) and (j not in (0,n-1))) or ((j==0 or j== n-1) and (i not in (0,n-1))):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
'''
n = int(input("enter the size: "))

for i in range(n):
    for j in range(n):
        if ((i==0 or i==n-1) and (j not in (0,n-1))) or ((j==0 or j== n-1) and (i not in (0,n-1))or (i==j and i>n//2)):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
