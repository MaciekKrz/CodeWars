def persistence(n):
    if len(str(n)) == 1:
        return 0
    list = [int(i) for i in (str(n))]
    result = 1
    result1= 1
    for i in list:
        result *= i
    if len(str(result)) == 1:
        return 1
    else:
        for j in str(result):
            result1 *= j
            print(result1)
            return 2
    return result






print(persistence(26))