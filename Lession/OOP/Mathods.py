class student : #class creating
    #default Constructor
    def __init__(self):
        pass
    #perametarized Constructor
    def __init__(self,name,roll,Section): 
        self.name = name
        self.roll = roll
        self.section = Section
        
#we need self perameter for mathods
    def display(self): 
        print(f"Student Name : {self.name}\nRoll : {self.roll}\nSection : {self.section}")
    def change_name(self,new_name):
        self.name = new_name
s1 = student("Helal",121,"C")
s1.display()
s1.change_name("Shohan")
s1.display()
s2 = student("Nuha",122,"D")
s2.display()

