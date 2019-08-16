L = int(input())
for i in range(1,L+1):
    for j in range(i,L+1):
        print(j,end="")
    print()
for i in range(1,L):
    for j in range(L-i,L+1):
        print(j,end="")
    print()