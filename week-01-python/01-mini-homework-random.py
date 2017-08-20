# 미니과제 01. 랜덤 뽑기

# list 만들기
list_a = [1, 2, 3, 4, 5]
tuple_a = (1, 2, 3, 4, 5)

# random 함수호출
import random

# random.choice 이용하여 임의의 값 하나 뽑기
print(random.choice(list_a))
print(random.choice(tuple_a))

# random.randint 사용하여 임의 값 뽑기
print(random.randint(1, 5))
