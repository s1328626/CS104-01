print ("simple counting loop with range")
names= []
for x in range(0,10):
    name = input("enter name: ")
    names.append(name)
print(names)

for x in range(0,10):
    name= len (names)
    print (names.pop(0))
    print (names)


