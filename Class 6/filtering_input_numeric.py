base_size = input("Enter the size of the triangle base as a whole integer value. >>>")

if not base_size.isnumeric():
    print("The amount must be a number, try again")
    exit()

# else:
#     print("Do something with amount entered")

if not float(base_size) % 1 == 0:
    print("The number isn't a integer")

if float(base_size) % 2 ==0:
    print("The number must be odd")
    exit()
