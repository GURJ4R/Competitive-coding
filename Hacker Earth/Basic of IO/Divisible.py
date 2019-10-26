n = int(input())
a = list(map(int, input().split()))
rem = 0
b=''
s=''
m=''
for i in range(n):
    if (i < (n // 2)):
        while (a[i]>=10):
            a[i]=a[i]//10
        b = b + str(a[i])
    if (i >= (n // 2)):
        rem = a[i]%10
        s=s+str(rem)
m=m+b+s
if (int(m)%11 == 0):
    print("OUI")
else:
    print("NON")






