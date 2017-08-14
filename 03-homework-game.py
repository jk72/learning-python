# 가위, 바위, 보 게임


# 컴퓨터 가위, 바위, 보 리스트에서 랜덤하게 뽑기 위해 random 함수 호출
import random

# 컴퓨터 가위, 바위, 보 리스트
list_b = ["가위", "바위", "보"]

# 이긴횟수, 진 횟수 카운팅 하기 위한 변수
person_win_count = 0
person_lose_count = 0

while person_win_count < 4 or person_lose_count < 4:
    # 가위, 바위, 보 입력 받기
    player = input("가위, 바위, 보 중 어떤 것을 낼래요? ")
    if player != "가위" and player != "바위" and player != "보":
        player = input("다시 입력해 주세요.(예: 가위, 바위, 보)")

    # 컴퓨터 가위, 바위, 보 임의 추출
    computer = random.choice(list_b)
    print("컴퓨터:", computer)

    # 사람과 컴퓨터간 가위, 바위, 보 비교 및 카운팅
    if player == computer:
        print("비겼습니다.")
    elif player == "가위":
        if computer == "바위":
            person_lose_count = person_lose_count + 1
            print("컴퓨터가 이겼습니다.")
        if computer == "보":
            person_win_count = person_win_count + 1
            print("당신이 이겼습니다.")

    elif player == "바위":
        if computer == "가위":
            person_win_count = person_win_count + 1
            print("당신이 이겼습니다.")
        if computer == "보":
            person_lose_count = person_lose_count + 1
            print("컴퓨터가 이겼습니다.")

    elif player == "보":
        if computer == "바위":
            person_win_count = person_win_count + 1
            print("당신이 이겼습니다.")
        if computer == "가위":
            person_lose_count = person_lose_count + 1
            print("컴퓨터가 이겼습니다.")

    # 3번 이겼는지, 3번 졌는지 조건비교, 최종결과, 게임종료
    if person_win_count == 3:
        print("당신이 3번을 이겼습니다.^^; 가위바위보 게임을 종료합니다.")
        break
    elif person_lose_count == 3:
        print("당신이 3번을 졌습니다.-_-; 가위바위보 게임을 종료합니다.")
        break
