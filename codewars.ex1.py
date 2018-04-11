# def get_middle(s):
#     print(int((len(s)/2)+2))
#     print(int(len(s)/2))
#     if len(s) % 2 == 0:
#         return s[int((len(s)/2)-1):int((len(s)/2)+1)]
#     else:
#         return s[int(len(s)/2)]



def get_middle(s):
   return s[(len(s)-1)/2:len(s)/2+1]


print(get_middle('A'))
