#Function_Definations
def sum(a,b): #parameters def funtion_name(para1,para2... ...)
    s = a+b
    return s
def ph(): #this is like void functions. it don't return anything
    print("hello from ph") 

a = int(input())
b = int(input())
print(sum(a,b)) #Arguments def funtion_name(argu1,argu2... ...)
a+=a #just to give different value
b+=b #just to give different value
calcu_sum = sum(a,b)
print(calcu_sum)
ph()
