file = open("fruits.txt", 'r')
fruits = file.readlines()
file.close()
for fruit in fruits:
    print(len(fruit.strip()))
