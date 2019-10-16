n = int(input())
for i in range(n):
    str1,str2 = input().split()
    d=[0]*26
    e=[0]*26
    for j in str1:
        d[ord(j)-97]+=1
    for k in str2:
        e[ord(k)-97]+=1
    if(d==e):
        print("YES")
    else:
        print("NO")

        
    
