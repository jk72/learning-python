# exceptions

# ZeroDivisionError
# 1 / 0
def divide_by(first, second):
    try:
        return first / second
    # except:
    except ZeroDivisionError:
        return "0으로 나눌 수 없습니다."

print(divide_by(4, 2))
print(divide_by(4, 0))
