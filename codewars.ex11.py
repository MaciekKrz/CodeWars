# def add_binary(a, b):
#     decNumber = (a + b)
#     binList = []
#
#     while decNumber > 0:
#         rem = decNumber % 2
#         binList.append(rem)
#         decNumber = decNumber // 2
#
#
#     return "".join(str(e) for e in binList[::-1])

def add_binary(a,b):
    return bin(a+b)[2:]

print(add_binary(2,2))


print(4.2/2)
print(4.2//2)