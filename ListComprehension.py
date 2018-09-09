# n = int(input())
lst = []
for x in range(int(input())):
    lst.append([input(), float(input())])
lst = sorted(lst, key=lambda x: x[1]);
for x in range(1, int(input())):
    if lst[x][1] != lst[x-1][1]:
        score = lst[x][1]
        break
lst = sorted(lst);
for x in range(int(input())):
    if(lst[x][1] == score):
        print(lst[x][0])