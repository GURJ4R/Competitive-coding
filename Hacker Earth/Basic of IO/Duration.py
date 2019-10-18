n=int(input())
c=0
l=0
for i in range(1,n+1):
    SH,SM,EH,EM=input().split()
    SH=int(SH)
    SM=int(SM)
    EH=int(EH)
    EM=int(EM)
    a=SH*60+SM
    b=EH*60+EM
    s=(b-a)
    while (s >= 60):
        c += 1
        s = s - 60
    print(c,s)
    c=0
    s=0
