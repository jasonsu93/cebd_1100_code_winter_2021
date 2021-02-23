# x = 5 / 0


def divide_numbers(n1:float, n2:float):

    try:
        result = n1 / n2
        return result
    except:

        return False

print(divide_numbers(7.0))