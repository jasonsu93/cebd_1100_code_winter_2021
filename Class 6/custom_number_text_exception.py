def is_a_float(n):
    try:
        float(n)
        return True
    except:
        return False

if not is_a_float("5"):
    print("This number is not a numeric")
else:
    print("The number IS a numeric")