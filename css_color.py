"""
Function checking proper css colors (RGB format) in input.
"""
import sys
import re


def css_color(line):
    match = re.findall(r'#[a-fA-F0-9]{3,6}\b[^\n]', line)
    if len(match) == 1:
        print(match[0][:-1])
    elif len(match) > 1:
        i = 0
        while i < len(match):
            print(match[i][:-1])
            i += 1
    else:
        return None


for line in sys.stdin:
    if css_color(line) is not None:
        css_color(line)
