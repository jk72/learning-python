# 사용자로 부터 값 받기
num_01 = int(input("몇 단을 출력하시겠습니까? "))

# 구구단 계산
for num_02 in range(1, 10):
    result = num_01 * num_02
# 구구단 입력 제한 (2에서 9까지만 입력하도록 제한하기)
    if num_01 < 10:
        print(num_01, " *", num_02, "=", result)
        
