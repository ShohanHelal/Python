# del keyword is delete the object
class student:
    def __init__(self,name) :
        self.name = name
        
s1 = student("Shohan")
print(s1.name)
del s1 #it will delete s1.
print(s1.name) 
