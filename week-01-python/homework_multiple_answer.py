# 사용자로 부터 몇 단을 출력할 지 받기
dan = int(input("몇 단을 출력 하시겠습니까?"))

# 구구단 실행
if dan > 0 and dan < 10:
    for num in range(1, 10):
        print("{} * {} = {}".format(dan, num, dan*num))
else:
    print("1에서 9사이의 숫자를 넣어주세요.")
