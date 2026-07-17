class car:
    brandName = "BMW" #this is a Class Attributes
    def __init__(self,ownerName,date):
        self.name = ownerName #these are object Attributes
        self.date = date
    def display(self):
        print(f"Owner Name = {self.name}\nBuing date = {self.date}")
c1 = car("Arham","25 June")
c1.display()
    