# operators = ['+', '-']
# target = 100
#
# lines = ['1']
# for i in range(2, 10):
#     for j in range(len(lines)):
#         for op in operators:
#             lines.append(lines[j]+op+str(i))
#         lines[j] += str(i)
# for line in lines:
#     if eval(line) == target:
#         print((line, "=", target))

d, o ="123456789", ["", "+", "-"]
s = len(o)

#Code
f = lambda v: filter(eval, ("".join(d[i]+o[j//s**i%s]
                                  for i in range(9)) + v for j in range(s**8)))
print(*f("==100"),"",sep="\n")




# print(eval('123-45-67+89'))