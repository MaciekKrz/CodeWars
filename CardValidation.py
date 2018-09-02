import re


def is_valid(uid):
    start_with_456 = bool(re.match(r'^[4-6]{1}', uid))
    has_groups_in_4 = bool(re.search(r'\d{4}-\d{4}-\d{4}-\d{4}', uid))
    has_only_digits = bool(re.search(r'^[0-9\-]*$', uid))
    has_16_proper_elements = bool(len(uid) == 16 or len(uid.replace('-', '')) == 16)

    def is_proper(uid):
        uid = uid.replace('-', '')
        for i in uid:
            if uid[int(i):int(i)+4].count(i) >= 4:
                return False
        return True
    if start_with_456 and has_only_digits and has_16_proper_elements and is_proper(uid):
        if '-' in uid:
                if has_groups_in_4:
                    return 'Valid'
                else:
                    return 'Invalid'
        return "Valid"
    else:
        return "Invalid"


for _ in range(int(input())):
    print(is_valid(input()))
