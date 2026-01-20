n = int(input("Enter the Size Of the List :"))
lst = []
print("Enter the numbers :")
for i in range(n):                                      
    ele = int(input())
    lst.append(ele)
max = 0 
Sec_max = 0
for i in range(n):
    if max < lst[i] :
        max = lst[i]
for i in range(n):
    if Sec_max < lst[i]:
        if lst[i] == max :
            continue
        else : 
            Sec_max = lst[i]
print("The Second lergest Number is",Sec_max)