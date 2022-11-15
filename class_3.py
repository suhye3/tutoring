# 1. 비어있는 학생(Student) 클래스를 정의하시오.
# 2. 학생(Student) 클래스의 인스턴스를 생성하고, 본인의 이름 변수(ex.seyeon)로 바인딩하시오.
# 3. 학생(Student) 클래스에 (이름, 국어점수, 수학점수, 영어점수, 과학점수)를 받는 생성자를 추가하시오.
# 4. 학생(Student) 클래스에 각 과목 점수의 합을 구하는 get_sum() 함수를 추가하시오.
# 5. 학생(Student) 클래스에 과목 점수의 평균을 구하는 get_avg() 함수를 추가하시오,
# 5. (2)에서 생성한 인스턴스를 통해 (5)에서 만든 함수에 접근해 이름과 평균을 출력하시오.

class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    def get_sum(self):
        return self.korean + self.math + self.english + self.science

    def get_avg(self):
        return self.get_sum()/4 
    
suhye = Student('수혜', 100, 50, 50, 100)
print("합계 :", suhye.get_sum())
print("평균: ", suhye.get_avg())


# 1. 계산기(Calc)라는 클래스를 생성하시오.
# 2. 계산기(Calc) 클래스의 인스턴스를 생성하시오.
# 3. 계산기(Calc) 클래스에 연산자(operator), 첫번째 수, 두번째 수를 인자로 입력받는 생성자를 추가하시오.
# 4. 계산기(Calc) 클래스에 계산결과를 반환하는 calc()라는 함수를 추가하시오.
# -> 입력받은 연산자와 두 수를 이용해 계산하시오.
# -> -(뺄셈), /(나눗셈)은 큰 수를 기준으로 계산하도록 하시오. (min, max 내장 함수 사용 가능)
# 5. (2)에서 생성한 인스턴스에 각각 연산자와 두 수를 입력해주는데, 이는 사용자에게 직접 입력 받도록 하시오.
# 7. (4)에서 생성한 클래스 메소드를 이용해 결과값을 출력하시오.

class Calc:
    def __init__(self, operator, first, second):
        self.operator = operator
        self.first = first
        self.second = second

    def calc(self):
        ncalc = 0
        if self.operator == '+':
            ncalc = self.first + self.second
        elif self.operator == '*':
            ncalc = self.first * self.second
        elif self.operator == '-':
            ncalc = max(self.first, self.second) - min(self.first, self.second)
        elif self.operator == '/':
            ncalc = max(self.first, self.second) / min(self.first, self.second)
        return ncalc

noperator = input('연산지 입력: ')
nfirst = int(input('첫번째 수 입력: '))
nsecond = int(input('두번째 수 입력: '))

my_calc = Calc(noperator, nfirst, nsecond)

print('result: ',my_calc.calc())

