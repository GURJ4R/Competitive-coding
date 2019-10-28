n=int(input())
rem=0
j=0
for i in range(1,11):
    rem=n%10
    j=j+(rem*(11-i))
    n=n//10
if(j%11==0):
    print("Legal ISBN")
else:
    print("Illegal ISBN")
