def find_even_index(arr):
    for i in range(len(arr)):
        if sum(arr[0:i]) == sum(arr[i+1:]):
            return i
    return -1



arr = [1,100,50,-51,1,1]
print(find_even_index(arr))

print(arr[0:1])
print(arr[1:])