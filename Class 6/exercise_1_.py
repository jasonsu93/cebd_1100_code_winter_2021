def get_max(n1, n2, n3):
    if n1 > n2:
        maxi = n1
    elif n2 > n3:
        maxi = n2
    else:
        maxi = n3
    return maxi

print(get_max(8, 5, 3))



