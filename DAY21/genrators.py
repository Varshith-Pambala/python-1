'''
def reels():
    res =('1-100','101-200','201-300','301=-400','401-500','501-600','601-700')
    yield res[0]
    yield res[1]
    yield res[2]
    yield res[3]
    yield res[4]
    yield res[5]
    yield res[6]

feed = reels()
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))

'''

'''
def reels():
    res =('1-100','101-200','201-300','301=-400','401-500','501-600','601-700')
    for i in res:
        yield i

feed = reels()
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))
print(next(feed))

'''
'''
def reel():
    res = ('1-100','101-200','201-300','301-400','401-500','501-600')
    for i in res:
        yield i

feed = reel()
for i in feed:
    print(i)
    '''

''''
def factorial(n):
        
        for i in range(1,n+1):
              
            if n%1==0:
                yield i

res = factorial(18)
for i in res:
     print(i)
'''
'''''
prime numbers
def primnumbers(n):
    for i in range(2,n+1):
        if n%1==0:
            yield i

res = primnumbers(8)
for i in res:
    print(i)
'''
'''''
def primes(n):
    for i in range(2,n+1):
        for j in range(2,i//2+1):
            if i%j==0:
                break
        else:
            yield i

res = primes(50)
for i in res:
    print(i)


'''
'''
def fibonacci(n):
    if n==1:
        yield 0
    elif n >=2:
        a,b=0,1
        yield 0
        yield 1
    for i in range(n-2):
        c = a+b
        a = b
        b = c
res = fibonacci(4)
for i in res:
    print(i)
    
'''