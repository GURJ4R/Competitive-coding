a,b,c=input().split()
a=int(a)
b=int(b)
c=int(c)
count=0
for i in range(a,b+1):
    if(i%c==0):
        count=count+1
print(count)
    
