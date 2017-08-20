# 회사 조직도 만들기

# 사람 클래스
class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

# 직장 동료 클래스 - inheritance
class CompanyCollegue(People):
    # job_grade = "대리"
    def __init__(self, name, age, gender, job_grade):
        super().__init__(name, age, gender)
        self.job_grade = job_grade

# 인스턴스 생성
# people = People("정수현", "20", "여성")
# company_collegue = CompanyCollegue("정재국", "20", "남성")
company_collegue = CompanyCollegue("정수현", 20, "여성", "대리")

# print(people.name, people.age, people.gender)
print(company_collegue.job_grade)
print(company_collegue.__dict__)
