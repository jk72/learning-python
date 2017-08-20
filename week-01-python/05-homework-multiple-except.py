
# # 구구단 실행 함수
def multiplication():
    try:
        num_01 = int(input("몇 단을 출력하시겠습니까? "))

        # 구구단 계산 (입력은 2~9사이로 제한)
        if num_01 >=2 and num_01 < 10:
            for num_02 in range(1, 10):
                result = num_01 * num_02
                print("{} * {} = {}".format(num_01, num_02, result))
        else:
            # 2~9외 숫자를 입력했을 때 & 재귀함수 호출
            print("2에서 9사이의 숫자만 입력해주세요.")
            multiplication()

    # '2단'과 같이 문자가 들어간 입력을 했을 때 예외처리 & 재귀함수 호출
    except ValueError:
        print("2에서 9사이의 숫자만 입력해주세요. (예:'2단'이라고 입력하지 마세요)")
        multiplication()
    except:
        print("알 수 없는 에러가 발생하였습니다.")
        multiplication()

multiplication()
