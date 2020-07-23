# put your python code here
import math
x = int(input())
y = int(input())
z = int(input())
p = (x + y + z) / 2
S = p * (p-x) * (p-y) * (p-z)
print(math.sqrt(S))
