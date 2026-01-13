n = int(input("Enter The Size : "))
for row in range(n):
    for col in range(n-row):
        print("*",end ="")
    print()    