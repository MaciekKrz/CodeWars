m = input()
n = input()


def check_palidrome(word):
    result =[]
    if '-' in str(word):
        return False
    for x in word.split():
        if str(x) == str(x)[::-1]:
            result.append(True)
        else:
            result.append(False)
    return any(result)


print(check_palidrome(n))