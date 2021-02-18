provinces = {"QC" : "Quebec", "ON" : "Ontario"}

#provincelist = ["Quebec", "Ontario"]

#print(provincelist[0])

# print(provinces["QC"])
#
# print(provinces.get("QC"))

# print(provinces["XX"])

provincename = provinces.get("XX", "NOT FOUND")

print(provincename)