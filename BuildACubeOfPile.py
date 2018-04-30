def find_nb(n):
    m = 0
    return ((n**2)*((n+1)**2)) // 4
    # while n >= 1:
    #     m += n**3
    #     n -= 1
    # return m

print(find_nb(45))