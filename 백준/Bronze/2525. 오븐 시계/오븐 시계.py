a, b = map(int, input().split())
c = int(input())

b += + c

if (b / 60 != 0):
    a += int(b / 60)
    b = b % 60

if (a >= 24):
    a -= 24

print(a, b)
