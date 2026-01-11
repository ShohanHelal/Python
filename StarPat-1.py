for row in range(5):
    for col in range(row):
        print('*',end = "") # end for not going in new line.
    print("") # python print funtion end a line with a '\n' automaticly
n = int(input())
for i in range(n+1):
    for j in range(i):
        print("#",end="")
    print()    