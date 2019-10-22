n=int(input())
k=list(map(int,input().split()))
c=1
for i in k:
    c=(c*i)%(10**9+7)
print(c)
    

