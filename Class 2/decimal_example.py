import decimal
#must include both "decim"al" because it's a package with the function decimal. Must do it for all imports

a = decimal.Decimal("10.45")
print(a + 6)

b = decimal.Decimal(10.45)
print(b + 6)

print(type(a))
print(type(b))
print(type(8))



