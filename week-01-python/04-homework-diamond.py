# 숫자로 다이아몬드 그리기

for a in range(1, 6):
    a = a - 3
    if a < 0:
        a = -a
    print("0" * a + "1" * (5 - a * 2) + "0" * a)
