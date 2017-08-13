# 맛집 고르기
rest_name = input("한식, 중식, 일식 중 하나를 입력하세요.(예: 한식)" )

# list_restaurant = ["한식", "중식", "일식"]
# 각 음식종류별 식당 리스트
list_korean_rest = ["나주곰탕집", "광화문식당", "파이썬식당", "고향식당"]
list_chinese_rest = ["북경반점", "만리장성", "상해반점", "취홍"]
list_japanese_rest = ["도쿄스시", "이야자끼", "홋가이도", "혼슈"]

# 식당이름 임의 수출을 위해 random 함수 호출
import random

# 사용자 음식종류 입력 비교하여 식당 임의추천 if문
if rest_name == "한식":
    print(random.choice(list_korean_rest))
elif rest_name == "일식":
    print(random.choice(list_japanese_rest))
else:
    rest_name == "중식"
    print(random.choice(list_chinese_rest))
