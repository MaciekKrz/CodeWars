"""
ABCXYZ company has up to  employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs.

A valid UID must follow the rules below:

It must contain at least  uppercase English alphabet characters.
It must contain at least  digits ( - ).
It should only contain alphanumeric characters ( - ,  -  &  - ).
No character should repeat.
There must be exactly  characters in a valid UID.
"""
import re


def is_valid(uid):
    uid = ''.join(sorted(uid))
    has_2_or_more_upper = bool(re.search(r'[A-Z]{2,}', uid))
    has_3_or_more_digits = bool(re.search(r'\d{3,}', uid))
    has_10_proper_elements = bool(re.search(r'^[a-zA-Z0-9]{10}$', uid))
    no_repeats = not bool(re.search(r'(.)\1', uid))

    if has_2_or_more_upper and has_3_or_more_digits and has_10_proper_elements and no_repeats:
        return "Valid"
    else:
        return "Invalid"


for _ in range(int(input())):
    print(is_valid(input()))
