def square_digits(num):
    return int(''.join(str(int(d)**2) for d in str(num)))

# def square_digits(num):
#     ret = ""
#     for x in str(num):
#         ret += str(int(x)**2)
#     return int(ret)


num = (9119)
print(square_digits(num))
