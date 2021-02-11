#symbol for list = []

# colour = ["red", "green", "blue","yellow"]
# prime_numbers = [2,3,5,7,9,11,19]
# You can change the list after it's created

# Access by index
# print(colour[1])

# Iterate over the list (go through all options in the list)
# Enumerate over the list = Go one by one down the list and process
# for c in colour:
#     print(c)

# Every student has 2 grades available. A midterm and a final grade.
# These grades must be grouped together

# grades = [70, 72, 80, 81, 66, 67]

grades_better = [[70, 72], [80, 81], [66, 69]]

# for s in grades_better:
#     print(s)

for s in grades_better:
    grade_midterm = s[0]
    grade_final = s[1]
    average = (grade_midterm + grade_final) / 2
    print(average)
