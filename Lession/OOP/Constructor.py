#all classes have a function called __init__(), which is always executed when the class is being initiated 
class student : #class creating
    #default Constructor
    def __init__(self):
        pass
    #perametarized Constructor
    def __init__(self,name,roll,Section): #self refering to the own object. here s1
        self.name = name
        self.roll = roll
        self.section = Section
#self basically a name of the object. not referace. we can name it abcd bla..bla

        
s1 = student("Helal",121,"C")
print(s1.name)
print(f"Student Name : {s1.name}\nRoll : {s1.roll}\nSection : {s1.section}")

