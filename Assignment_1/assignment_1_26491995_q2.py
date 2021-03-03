table = int(input("What size multiplication table would you like printed? >>>"))
print(table)
print("Multiplication Table of",table)

for x in range(1, table+1):
    for y in range(1, table+1):
        print(x * y, end="\t")
    print("\n")

