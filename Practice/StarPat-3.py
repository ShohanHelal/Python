n = int(input())
for row in range(n):
    for j in range(n-row):
        print(" ", end ="")
    for k in range(row):
        print("*",end = "")    
    print("")    