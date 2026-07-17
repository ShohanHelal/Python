a = [1,2,3,4,5]
b = map(lambda x : x*2, a) #auto work, no need for loops
print(list(b))

c = [x*2 for x in a] # manual , like before
print(c)