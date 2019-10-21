n=int(input())
for i in range(2,n+1):
    for num in range(2,i):
        if(i%num==0):
            break
    else:
        print(i,end=" ")
    
