# def digital_root(n):
#     result = 0
#     while len(str(result))==1:
#         result = sum([int(i) for i in str(n)])
#         result = sum([int(i) for i in str(result)])
#         result = sum([int(i) for i in str(result)])
#         return result


def digital_root(n):
  return n%9 or n and 9

print(digital_root(94223337799999999999999999999999999))
print(16%9)