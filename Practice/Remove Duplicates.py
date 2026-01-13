n = int(input("Enter the Size Of the List :"))
lst = []
print("Enter the numbers :")
for i in range(n):                                      
    ele = int(input())
    lst.append(ele)
lst2 =[]
for i in range(n):
    f = False
    for j in range(len(lst2)):
        if lst[i] == lst2 [j]:
            f = True
            break
    if f == False :
        lst2.append(lst[i])
    else :
        continue
print("First List :",lst)
print("Second List :",lst2)
        
    