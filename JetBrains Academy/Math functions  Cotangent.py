import math
x = int(input())
res = 1 / math.tan(math.radians(x))  
print("{:.10f}".format(res))