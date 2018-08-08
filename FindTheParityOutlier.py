# def find_outlier(integers):
#     if (integers[0]%2 + integers[1]%2 + integers[2]%2) <=1:
#         for i in integers:
#             if i%2!=0:
#                 return i
#     else:
#         for i in integers:
#             if i%2==0:
#                 return i

def find_outlier(integers):
    parity = [n % 2 for n in integers]
    return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]


integers = [-3416889, 2912144, -6190794, -8707804, -969416, 6666108, -1075280, 4194018, -996436, -1751164, 8654556,
             3257336, -1842740, -5159670, 5767624, -4894972, 5309342, 5070364, -6819174, 7892082, -2069204, -5839522,
             6450940, 398048, -4123802, 6055314, -5514580, -8546236, -6414986, -8379590, -1812962, 5442684, -1891516,
             -6180532, 3115704, 2599564]
print(integers.index(2))

print(find_outlier(integers))
