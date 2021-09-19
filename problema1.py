a=[1,2,3,4,5]
print(a[0]+a[1]+a[2])
b=a
print(sum(b))
p=1
for i in range(0,len(a)):
    p=p*a[i]
print(p)
print(b[2])
print(a[0]+b[0])