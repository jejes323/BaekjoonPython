NumberList = []

for i in range (9):
    NumberList.append(int(input()))

print(max(NumberList))
print(NumberList.index(max(NumberList)) + 1)