empty = []
x = int(input())
for _ in range(x):
    inp = str(input())
    if inp.split()[1] == 'win':
        empty.append(inp.split()[0])
print(empty)
print(len(empty))
