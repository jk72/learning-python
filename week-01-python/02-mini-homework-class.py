# 학교 클래스 만들기
class School:
    def __init__(self, school_name, year, address):
        self.school_name = school_name
        self.year = year
        self.address = address

school = School("파이썬고", "1991", "네덜란드")

print(school.school_name)
print(school.year)
print(school.address)
