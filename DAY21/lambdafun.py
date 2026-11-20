'''''


d = {'a':500,"b":200,'c':1000,"d":1300}

s = {"s1":True,"s2":False,"s3":True,"s4":True,"s5":False}

gst = dict(map(lambda i:(i[0],i[1]+i[1]*0.18),d.items()))

gre = dict(filter(lambda i:i[1]>500,d.items()))

booked = dict(filter(lambda i:i[1]==True,s.items()))

unbooked = dict(filter(lambda i:i[1]!=True,s.items()))

print(gst)
print(gre)
print(booked)
print(unbooked)

'''''

'''''

d = {'laptop':90000,'keyboard':2000,'camera':100000,'mouse':1300}

print(dict(sorted(d.items())))
print(dict(sorted(d.items(),reverse=True)))

print(dict(sorted(d.items(),key=lambda i:i[1])))
print(dict(sorted(d.items(),key=lambda i:i[1],reverse=True)))

'''

