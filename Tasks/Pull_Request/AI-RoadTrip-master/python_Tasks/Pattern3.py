L =  int(input())
for i in range(1,L+1):
    for j in range(0,L-i):
        print(" ",end="")
    for k in range(1,i+1):
        print(k,end="")
    for z in range(i-1,0,-1):
        print(z,end="")
    print()