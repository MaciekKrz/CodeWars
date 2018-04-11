import re

s = "The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog"


print(re.findall(r"(\d+)", s))
    