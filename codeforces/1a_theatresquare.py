import math

n, m, a = [int(i) for i in raw_input().split(" ")]
rows = math.ceil(float(m) / a)
cols = math.ceil(float(n) / a)
print int(rows * cols)
