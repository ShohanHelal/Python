
while True:
 a = float(input("Enter The first Value : "))
 b = float(input("Enter The Second Value : "))
 c = input("Enter The Oparator(+,-,*,/) : ")
 if c =='+':
    print("The Answer is :",a+b)
 elif c =='-':
    print("The Answer is :",a-b)
 elif c =='*':
    print("The Answer is :",a*b)
 elif c =='/':
    if b==0:
        print("Math error")
    else:    
        print("The Answer is :",a/b)
else:
   print("Invalide Sele") 