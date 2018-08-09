def iq_test(numbers):
    x = numbers.split()
    parity = [int(n)%2 for n in x]
    return (parity.index(1)+1) if sum(parity) == 1 else (parity.index(0)+1)


# def iq_test(numbers):
#     e = [int(i) % 2 == 0 for i in numbers.split()]
#     return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1


numbers = "1 2 2"
print(iq_test(numbers))
# print(map(numbers.split()))