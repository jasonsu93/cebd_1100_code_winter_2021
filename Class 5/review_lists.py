#1 Create a list with numbers 0 to 9 in it
#2 Display the list elements separated by a comma (comma at end ok)
#3 Display all even elements of the list
#4 Display the average value of all elements in the list

#1 Create the list
list1 = list(range(10))
print(list1)

#2 Display elements
for x in list1:
    print(str(x) + ",")

for x in list1:
    print(str(x), end=",")

#3 Display even elements
for x in list1:
   if x % 2 == 0:
    print(x)

#4 Average value of elements
print(sum(list1) / len(list1))

