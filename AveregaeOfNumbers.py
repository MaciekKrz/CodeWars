def averages(arr):
    result = []
    i=0
    while i < (len(arr)-1):
        result= arr[i] + arr[i+1]
        i+=1
    return result
    # return sum(arr[i][i] +(arr[i][i+1]) for i in arr)

tests =[1, 3, 5, 1, -10]

print(averages(tests))