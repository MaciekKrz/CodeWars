# Task of this function is to move first element of string to last position until all elements are moved.
# Example: [Input]: 'Hello' [Output]: 'elloH', 'lloHe', 'loHel', 'oHell', 'Hello'


def string_rotation(string):
    x = 1
    result = []
    while x <= len(string):
        list1 = string[x:] + string[:x]
        result.append(list1)
        x += 1
    return result


print(string_rotation('Hello'))
print(string_rotation('This is major problem'))
