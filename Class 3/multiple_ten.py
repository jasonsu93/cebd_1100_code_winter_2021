# Multiples of Ten: Ask the user for a number,
# and then report whether the number is a multiple of 10 or not

#modify this assignment in order to do it in a loop
# the loop should end once the user presses "q" or "Q"

# answer = ""
#
# while True:
#     answer = input("Enter a number")
#     # if answer == "q" or answer == "Q":
#     #     break
#     if answer.upper() == "Q":
#         break
#
#     if int(answer) % 10 == 0:
#         print(answer + "is a multiple of 10")
#     else:
#         print(answer + "is not a multiple of 10")

answer = ""
while True:
    answer = input("Enter a number >>>")
    if answer == "q" or answer == "Q":
        break
    if int(answer) % 10 == 0:
        print(answer + "is a multiple of 10")
    else:
        print(answer + "is NOT a multiple of 10")
