str=input()
s=len(str)
c=0
for i in range(0,s):
    if(str[i]==str[s-1-i]):
        c=c+1
if(c>=s/2):
    print("YES")
else: 
    print("NO")
