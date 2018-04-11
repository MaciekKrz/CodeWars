# def is_divisible(n, *args):
    # return len(list([i for i in args if n%i==0]))== len(args)

def is_divisible(n, *args):
    return all(not n % i for i in args)

print(is_divisible(6,2,3,4))
