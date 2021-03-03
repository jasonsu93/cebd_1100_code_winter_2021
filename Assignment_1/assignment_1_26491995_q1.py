def left_asterisk_triangle(n):
    x = 1
    while (x <= n):
        print("*" * x)
        x = x + 1

def create_pyramid(n):
    for i in range(n):
        print((" " * (n - i - 1) + "*" * (2 * i + 1)))


if __name__ == "__main__":
    while True:
        print("1: Draw a Triangle")
        print("Q: Quit")
        menu1 = input("Enter a choice >>>")

        if menu1 == "1":
            while True:
                print("1: Right sided Triangle")
                print("2: Iso Triangle")
                print("Q: Back")
                menu2 = input("Enter a choice >>>")
                if menu2 == "1":
                    n = int(input("Please enter the size of the base of the triangle >>>"))
                    left_asterisk_triangle(n)
                elif menu2 == "2":
                    n = int(input("Please enter the size of the triangle >>>"))
                    # iso_asterisk_triangle(n)
                    create_pyramid(n)
                elif menu2 == "Q":
                    print("Going to Previous Menu")
                    break
        else:
            print("Exiting Program")
            break






