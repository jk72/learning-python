# 사칙연산 계산 클래스
class fourcal:

# 두 숫자 입력 받는 함수
    def setdata(self, first, second):
        self.first = first
        self.second = second

# 더하기 계산 함수
    def sum(self):
        result = self.first + self.second
        return result

# 곱하기 계산 함수
    def mul(self):
        result = self.first * self.second
        return result

# 빼기 계산 함수
    def sub(self):
        result = self.first - self.second
        return result

# 나누기 계산 함수
    def div(self):
        result = self.first / self.second
        return result

a = fourcal()
b = fourcal()
print(type(a))

a.setdata(4, 2)
print(a.sum())

b.setdata(3, 7)
print(b.sub())
