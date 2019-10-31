n=int(input())
a=list(map(int,input().split()))
rem=0
b=' '
for i in range(0,n):
    rem=a[i]%10
    b=b+str(rem)
if(int(b)%10==0):
    print("Yes")
else:
    print("No")
