a, b, c = map(int, input().split())

if(a == b == c):
    money = 10000 + a * 1000
elif(a == b or a == c or b == c):
    if(a == b):
        money = 1000 + a * 100
    elif(a == c):
        money = 1000 + a * 100
    elif(b == c):
        money = 1000 + b * 100
elif(a != b != c):
    if ( a > b and a > c):
        money = a * 100
    elif (b > a and b > c):
        money = b * 100
    elif (c > a and c > b):
        money = c * 100

print(money)