# ✅↓ Write your code here ↓✅

def number_of_bottles():
    bottles = int(99)

    for i in range(bottles):
        if(bottles == 2):
            print("2 bottles of milk on the wall, 2 bottles of milk.")
            bottles -= 1
            print("Take one down and pass it around, 1 bottle of milk on the wall.")
        elif(bottles == 1):
            print("1 bottle of milk on the wall, 1 bottle of milk.")
            bottles -= 1
            print("Take one down and pass it around, no more bottles of milk on the wall.")
        elif(bottles == 0):
            print("No more bottles of milk on the wall, no more bottles of milk.")
            bottles -= 1
            print("Go to the store and buy some more, 99 bottles of milk on the wall.")
        else:
            print(str(bottles) + " bottles of milk on the wall, " + str(bottles) + " bottles of milk.")
            bottles -= 1
            print("Take one down and pass it around, " + str(bottles) + " bottles of milk on the wall.")

number_of_bottles()
