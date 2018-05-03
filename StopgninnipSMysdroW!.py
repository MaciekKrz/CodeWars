# def spin_words(sentence):
#     list = []
#     for i in sentence.split(" "):
#         if len(i)>=5:
#              list.append(i[::-1])
#         else:
#             list.append(i)
#     return " ".join(list)


def spin_words(sentence):
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])


print(spin_words("This is another test"))

# s = "This is another test"
#
# print(s.split(" "))