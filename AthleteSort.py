'''
You are given a spreadsheet that contains a list of  athletes and their details (such as age, height, weight and so on).
 You are required to sort the data based on the th attribute and print the final resulting table.
  Follow the example given below for better understanding.

image

Note that  is indexed from  to , where  is the number of attributes.

Note: If two attributes are the same for different rows, for example, if two atheletes are of the same age,
print the row that appeared first in the input.

Input Format

The first line contains  and  separated by a space.
The next  lines each contain  elements.
The last line contains .
'''

nm = input().split()

n = int(nm[0])

m = int(nm[1])

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

k = int(input())
x =[]
l = 0
sorted_arr = sorted(arr, key=lambda arr: arr[k])
for i, value in enumerate(sorted_arr):
    # print(i)
    for j in value:
        l += 1
        print(j, end='{}'.format('\n'if int(l)%int(m) == 0 else ' '))
