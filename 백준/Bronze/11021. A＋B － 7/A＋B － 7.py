import sys

n = int(sys.stdin.readline())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%s: %s"%(i + 1, a+b))