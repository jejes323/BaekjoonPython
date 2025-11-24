# 두 수 입력 받기
a, b = input().split()

# 각 수를 거꾸로 뒤집기 (문자열 슬라이싱 사용)
reversed_a = int(a[::-1])
reversed_b = int(b[::-1])

# 더 큰 수 출력
print(max(reversed_a, reversed_b))
