x = input()
li = list(x)
length = len(li) - 1
empty = []

for i in range (length):
    num = int(li[i]) + int(li[i+1])
    num = num / 2
    empty.append(num)

print(empty)
