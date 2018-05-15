def duplicate_encode(word):
    return ''.join(")" if word.lower().count(j) > 1 else "(" for j in word.lower())



print(duplicate_encode("nGdb!QJIn)PaQFduTSbOa"))
x = "nGdb!QJIn)PaQFduTSbOa"
print(x.lower())