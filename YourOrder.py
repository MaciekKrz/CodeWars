def order(sentence):
  result = []
  for i in range(1,10):
      for item in sentence.split():
         if str(i) in item:
            result.append(item)
  return result


# def order(sentence):
#     return " ".join(sorted(sentence.split(), key=lambda x: int(filter(str.isdigit, x))))


sentence = "is2 Thi1s T4est 3a"
print(order(sentence))
