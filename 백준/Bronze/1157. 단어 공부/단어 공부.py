word = input().upper()

# 빈도수를 세면서 동시에 최대 빈도수와 해당 문자들 추적
freq = {}
max_count = 0
max_chars = []

for char in word:
    # 빈도수 증가
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1


# 빈도수가 가장 많은 값 찾기
max_count = 0
for count in freq.values():
    if count > max_count:
        max_count = count

# 최대 빈도수를 가진 문자들 찾기
max_chars = []
for char, count in freq.items():
    if count == max_count:
        max_chars.append(char)


# 결과 출력
if len(max_chars) > 1:
    print('?')
else:
    print(max_chars[0])
