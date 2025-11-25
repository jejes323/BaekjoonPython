n = int(input())

# 위쪽 절반 (1번째 줄부터 N번째 줄까지)
for i in range(1, n + 1):
    for f in range(0, n-i):
        print(' ', end='')
    for s in range(0, 2*i-1):
        print('*', end='')
    print()  # 줄바꿈
    

# 아래쪽 절반 (N+1번째 줄부터 2*N-1번째 줄까지)
for i in range(n - 1, 0, -1):
    print(' ' * (n - i), end='')
    print('*' * (2 * i - 1))
