def stray(arr):
    x =  sorted(arr)
    if x[0] != x[-1] and x[0]==x[1]:
        return x[-1]
    else:
        return x[0]




arr = [1, 1, 2]

print(stray(arr))