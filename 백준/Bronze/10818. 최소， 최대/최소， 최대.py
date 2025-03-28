import sys

a = int(sys.stdin.readline())
listcase = list(map(int, sys.stdin.readline().split()))

max = listcase[0]
min = listcase[0]

for i in listcase:
    if(i > max):
        max = i
    elif(i < min):
        min = i
    
print(min, max)