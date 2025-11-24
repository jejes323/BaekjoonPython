# 올바른 체스 피스 개수
king = 1
queen = 1
rook = 2
bishop = 2
knight = 2
pawn = 8

# 입력 받기
fount = list(map(int, input().split()))

# 필요한 개수 계산
need_king = king - int(fount[0])
need_queen = queen - int(fount[1])
need_rook = rook - int(fount[2])
need_bishop = bishop - int(fount[3])
need_knight = knight - int(fount[4])
need_pawn = pawn - int(fount[5])

# 결과 출력 (공백으로 구분)
print(need_king, need_queen, need_rook, need_bishop, need_knight, need_pawn)
