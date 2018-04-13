def get_issuer(number):
  if str(number)[0:2] == '34' or str(number)[0:2] == '37':
      if len(str(number)) == 15:
          return "AMEX"
      else:
          return "Unknown"
  elif str(number)[0:4] == '6011' and len(str(number)) == 16:
      return "Discover"
  elif str(number)[0:2] in ['51', '52', '53', '54', '55'] and len(str(number)) == 16:
      return "Mastercard"
  elif str(number)[0] == '4':
      if len(str(number)) == 13 or len(str(number)) == 16:
          return "VISA"
      else:
          return "Unknown"
  else:
      return "Unknown"


print(get_issuer(3796455021609))

x =4111111111111111
print(str(x)[0:2])
