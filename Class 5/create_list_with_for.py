# list1 = [2, 4, 7, 9]
#
# # for value in list1:
# #     print(value)
#
# list2 = [value for value in list1]
# list3 = [value + 1 for value in list1]

daily_sales = [10.99, 12.99, 1.99, 2.39]

daily_tax_paid = [value * 0.1556 for value in daily_sales]

print(daily_sales)
print(daily_tax_paid)





# squares = [values + 1 for values in range(1,11)]