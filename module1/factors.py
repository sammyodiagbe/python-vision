def getFactors(number):
    list_of_factors = []
    if number == 1:
        return [1]
    if number == 0:
        return 'Invalid 0 can\'t be accepted'
    for x in range(1, number):
        if number % x ==  0:
            list_of_factors.append(x)

    return list_of_factors

print(getFactors(12))