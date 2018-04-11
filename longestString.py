def longest(words):
    return max(len(i) for i in words)

words = ['simple', 'is', 'better', 'than', 'complex']

print(longest(words))