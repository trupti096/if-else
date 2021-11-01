a=[1,2,3,4,[5,6,7],8]
i=0
b=[]
while i<len(a):
    if a[i]=="4":
        j=0
        while j<len(a[i]):
            sum=a[i]+a[4][0]+a[4][1]+a[4][2]
            j=j+1
        b.append(sum)
        a.insert(4,b)
    i=i+1
print(sum)