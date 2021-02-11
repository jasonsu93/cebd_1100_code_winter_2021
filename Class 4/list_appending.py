# Enter number of items received in shipment

item_count = 0
item_list = []

while item_count != -1:

    item_count = int(input("Enter item count. Enter -1 to stop. >>>"))

    if item_count > 0:
        item_list.append(item_count)

print("The total items added are ", end ="")
print(sum(item_list))