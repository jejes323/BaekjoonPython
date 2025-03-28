import sys

a , b = map(int, sys.stdin.readline().split())
listcase = list(map(int, sys.stdin.readline().split()))

for i in listcase:
    if (b > i):
        print(i, end = " ")