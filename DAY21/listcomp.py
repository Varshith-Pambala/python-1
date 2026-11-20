'''''
res = [i for i in range(1,11)]
print(res)

n = 15
fact = [i for i in range(1,n+1)if n%i==0]
print(fact)

name = ['bannu','baddu', 'deepika','varshith','varun']
res = [i for i in name if i .startswith('b')]
print(res)

l=[1,2,3,4,5,7,68,34,54,76,75,1,2,3,5,6]
res = [i if i%2==0 else 0 for i in l]
print(res)

nes = [[j for j in range(1,4)]for i in range(5)]
print(res)

'''

res = {i for i in range(1,11)}
print(res)

n = 15
fact = { i for i in range(1,n+1)if n%i==0}
print(fact)