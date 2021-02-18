provinces = {"QC" : "Quebec", "ON" : "Ontario"}

#Add a new province

provinces["BC"] = "British Columbia"

# print(provinces)

# del(provinces["BC"])
#
# print(provinces)

# Print the following: QC is Quebec, ON is Ontario

# for x in provinces:
#     print(x)

# for x in provinces.items():
#     print(x)

# The above code will give you a tuple

# for x in provinces.items():
#     print(x[0] + " is " + x[1])

# for x, y in provinces.items():
#     print(x + " is " + y)
#
# for x in provinces.values():
#     print(x)
#
# for x in provinces.keys():
#     print(x)

# print(provinces.keys())
# print(provinces.values())


# print("QC" in provinces)
# print("XX" in provinces)
#
#
# students = [student1, student2]
#
# student_list = {1234567: student1, 223456: student2}

product_grade = {1:"New", 2:"Used", 3:"Refurbished"}
print(product_grade[2])
print(type(product_grade))