

while True:
    print("A: Student menu")
    print("B: instructor menu")
    print("Q: Quit")
    menu1 = input("Enter a choice >>>")

    if menu1 == "A":
        while True:
            print("Student Menu")
            print("A: View grades")
            print("B: Modify course")
            print("Q: Quit")
        menu1 = input("Enter a choice >>>")

        if menu_student == "B":
            tuition_amount = input("Enter amount to be paid today")

            if not tuition_amount.isnumeric():
                print("The amount must be a number, try again")
            else:
                print("Do something with amount entered")

        if menu_student == "Q":
            print("Go to previous menu")
            break


    #
    # if menu1 == "Q":
    #     print("Exiting program")
    #     break
