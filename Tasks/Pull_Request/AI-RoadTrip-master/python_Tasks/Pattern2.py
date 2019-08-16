L = int(input())
for i in range(1,L+1):
    for j in range(L-i):
        print(" ",end="")
    for k in range(i):
        print("# ",end="")
    print()


# Alternate Method using python string ability.

# L = int(input())
# for i in range(1,L+1):
#     print(" "*(L-i),end="")
#     print("# "*i)

    