# 단어의 개수 입력받기
n = int(input())

# 그룹 단어의 개수를 세는 변수
group_word_count = 0

# n개의 단어를 하나씩 확인
for i in range(n):
    word = input()  # 단어 입력받기
    
    # 이 단어가 그룹 단어인지 확인하는 변수
    is_group_word = True
    
    # 이미 나온 문자들을 저장하는 리스트
    already_appeared = []
    
    # 단어의 각 문자를 하나씩 확인
    for j in range(len(word)):
        current_char = word[j]  # 현재 문자
        
        # 첫 번째 문자이거나, 이전 문자와 같으면 계속 진행
        if j == 0 or word[j] == word[j-1]:
            # 첫 번째 문자인 경우에만 리스트에 추가
            if j == 0:
                already_appeared.append(current_char)
        else:
            # 이전 문자와 다른 문자가 나왔을 때
            # 이 문자가 이미 나온 적이 있는지 확인
            if current_char in already_appeared:
                # 이미 나온 문자라면 그룹 단어가 아님
                is_group_word = False
                break  # 더 이상 확인할 필요 없음
            else:
                # 새로운 문자라면 리스트에 추가
                already_appeared.append(current_char)
    
    # 그룹 단어라면 개수 증가
    if is_group_word:
        group_word_count += 1

# 결과 출력
print(group_word_count)
