def generate_salutation(first: str, last: str = "Unknown"):
    return "Hello" + first + last

print(generate_salutation("Jason", "Su"))

def add_two_numbers(num1 = 0, num2 = 0):
    return num1 + num2
num2 = add_two_numbers(6, "Jack")

