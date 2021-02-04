# Keep asking the user for a number (integer)
# Keep track of the sum of the numbers added
# When the user enters "-1" then stop and print the sum of all numbers entered

sum_of_numbers = 0
entered_value = ""

#the_result = 0
#while the_result != -1:
#    the_result = int(input("number:"))
#    sum_of_numbers=sum_of_numbers+the_result
#print(sum_of_numbers+1)

while True:
    entered_value = int(input("enter a number >>"))
    if  entered_value == -1:
        break
    else:
        sum_of_numbers += entered_value





