# def get_sum(a=0,b=0):
#     if a==b:
#         return a
#     result = 0
#     if a < b:
#         for i in range(a,b+1):
#           result += i
#         return result
#     if b < a:
#         for i in range(b,a+1):
#           result += i
#         return result

def get_sum(a,b):
    return sum(range(min(a,b), max(a,b)+1))

print(get_sum(-1,1))