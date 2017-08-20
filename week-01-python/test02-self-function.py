def main():
    num = int(input("자연수를 입력해 주세요.\n"))
    fact = factorial(num)
    print("자연수", num, "의 계승은", fact)

def factorial(num):
    if num == 0:
        return 1
    else:
        return factorial(num)

main()
