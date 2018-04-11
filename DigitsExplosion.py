def explode(s):
    return ''.join(str(i)*int(i) for i in s)


print(explode("312"))