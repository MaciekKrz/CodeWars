def high_and_low(numbers):
    nn = [int(s) for s in numbers.split(" ")]
    return "{} {}".format(max(nn), min(nn))



print(high_and_low("5 1 2 3 4 5"))
