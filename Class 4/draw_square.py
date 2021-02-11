# Ask the user how big the square should be, then draw the square
# use *2* methods to do this Method 1: using nested loops, Method 2: using the multiplcation symbol
# use the "#" character to draw the square


size = int(input("What is the size of the square? >>>"))

#Method 1
for y in range(0, size):
    for x in range(0, size):
        print("%", end="")
    print()



#Method 2
for x in range(0, size):
    print("#" * size)



