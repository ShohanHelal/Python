n = int(input("Size of the list :"))
lst = []
p = 0
ne = 0 
z = 0
print("Enter the elements of the List :")
for i in range(n) :
    ele = int(input())
    lst.append(ele)
    if ele > 0 :
        p +=1
    elif ele <0 :
        ne +=1
    elif ele == 0 :
        z += 1
              
print("Positive :",p)
print("Negative :",ne)
print("Zeros :",z)    