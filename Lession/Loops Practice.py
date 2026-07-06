n = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter The Number You are Searching For :"))
for i in range(len(n)):
    if n[i] == x:
        print("Number Found in",i)
        break