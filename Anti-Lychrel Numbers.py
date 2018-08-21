# Write a program to check of the user input is an anti-Lynchrel number or not.
# Example: [Input]: 12 [Output]: True(12 + 21 = 33, a palindrome)


def anti_lychrel_number(num):
    i = 1
    sum = num + int(str(num)[::-1])
    while i <= 30:
        sum = sum + int(str(sum)[::-1])
        i += 1
        if str(sum) == str(sum)[::-1]:
            return '{} is Anti-Lyncher Number after:{} iterations'.format(num, i)
    return '{} is not Anti-Lyncher Number'.format(num)


print(anti_lychrel_number(57))
