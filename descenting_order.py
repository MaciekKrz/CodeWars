def Descending_Order(num):
    return "".join(sorted(list(str(num))))[::-1]


num = 293448383
x = "".join(sorted(list(str(num))))[::-1]
print(x)