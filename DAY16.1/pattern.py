#n = int(input("enter the size: "))
#for row in range(n):
#    for sp in range(n-1-row):
#        print(' ',end=' ')
#    for col in range(row+1):
#        print('*',end=' ')
#   print()

#n= int(input("enter the size: "))
#for row in range(n):
#    for sp in range(row):
#        print(' ',end=' ')
#    for col in range(n-row):
#        print('*',end=' ')
#    print()

#n= int(input("enter the size: "))
#m= n//2
#for row in range(n):
#    if row <=m:
#        for col in range(row+1):
#            print('*',end=' ')
#    else:
#        for col in range(n-row):
#            print('*',end=' ')
#    print()

#n = int(input("enter the size: "))
#m = n//2
#for row in range(n):
#    if row <=m:
#        print('*',end=' ')
#    else:
#        print('*',end=' ')
#    print()

#n = int(input("enter the size: "))
#m = n//2
#for row in range(n):
#    print('* '*(row+1) if row <= m else '* '*(n-row))
    
#n = int(input("enter the size: "))
#for row in range(n):
#    for col in range(n):
#        if row ==0 or col ==0 or row ==n-1 or col ==n-1:
#            print('*',end=' ')
#        else:
#            print(' ',end=' ')
#        print()

#n = int(input("enter the size: "))
#m= n//2
#for row in range(n):
#    for col in range(n):
#        if row ==0 or col ==0 or row ==n-1 or col ==n-1 or row ==m-n or col ==m-n:
#            print('*',end=' ')
#        else:
#            print(' ',end=' ')
#    print()

#n = int(input("enter the size:"))
#m= n//2
#for row in range(n):
#    for col in range(n):
#        if row ==0 or col ==0 or row ==n-1 or col ==n-1 or row ==m or col ==m:
#            print('*',end=' ')
#        else:
#            print(' ',end=' ')
#    print()

#n= int(input("enter the size: "))
#m= n//2
#for row in range(n):
#    for col in range(n):
#        if row== 0 or col ==0 or row ==n-1 or col ==n-1 or row ==m or col ==m or row ==col or row+col ==n-1:
#            print('*',end=' ')
#        else:
#            print(' ',end=' ')
#        print()

#n= int(input("enter the size: "))
#m= n//2
#for row in range(n):
#    for col in range(n):
#        if row ==0 or col ==0 or row ==n-1 or(col ==n-1 and row>=n) or (row==n and col>=m):
#            print('*',end=' ')
#        else:
#            print(' ',end=' ')
#    print()

#n= int(input("enter the size: "))
#m= n//2
#for i in range(n):
#    for j in range(n):
#        if i==0 or j==m or (i==n-1 and j<=m) or (j==0 and i>=m):
#            print('*',end=' ')
#        else:
#            print(' ',end=' ')
#    print()

#n = int(input("Enter the size: "))
#m = n//2
#for i in range(n):
#    for j in range(n):
#        if j==0 or j==n-1 or (i==j and i<=m) or (i+j==n-1 and i<=m):
#            print('*',end=' ')
#        else:
#            print(' ',end=' ')
#    print()

n = int(input("enter the size: "))
m = n//2
for i in range(n):
    for j in range(n):
        if j==0 or i==0 or i <=m or j>=m or (i+j==n-1 and i<=m):
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()