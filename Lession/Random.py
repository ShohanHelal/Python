import random

#This for Integer Value
num = random.randint(1,10) 
print(num) 

#This for float Value(it's take no argument only 0.0 to 1.0)
num = random.random()
print(num)

#Random Float in a Range
num = random.uniform(10, 20)
print(num)

#Random Choice from a List
fruits = ["Apple", "Banana", "Orange", "Mango"] 
fruit = random.choice(fruits)
print(fruit)