
n=int(input("Enter number:"))
for i in range(1, n + 1):
  for k in range(1, i): 
            print(" ", end = "")
  for j in range(i, n + 1):  
            print(j, end = " ")  
  print() 

for i in range(n- 1, 0, -1):
   for k in range(1, i): 
            print(" ", end = "")
   for j in range(i, n + 1): 
            print(j, end = " ") 
   print()
