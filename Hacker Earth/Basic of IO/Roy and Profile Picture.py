L=int(input())
N=int(input())
for i in range(1,N+1):
    W,H=input().split()
    W=int(W)
    H=int(H)
    if(W==H and W>=L):
        print("ACCEPTED")
    elif((W>L and H>=L) or (W>=L and H>L)):
        print("CROP IT")
    else:
        print("UPLOAD ANOTHER")
