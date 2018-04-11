def has_unique_chars(string):
  for i in string:
      s = string.replace(i, '')
      if len(string) == (len(s)+2):
          return False
  return True



print(set('dsddfdfsdfsdfsdf'))