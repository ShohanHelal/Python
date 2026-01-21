n = int(input("Enter the Size Of the List :"))
lst = []
sum = 0
print("Enter the numbers :")
for i in range(n):
    ele = int(input())
    lst.append(ele)
    if ele % 2 == 0 :
        sum = sum+ele
    else:
        continue    
print("The Sum Of All Even Number Of The List :",sum)