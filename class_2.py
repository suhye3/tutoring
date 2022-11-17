# 1. 비어있는 사람(Human) 클래스를 정의하시오.
# 2. 사람 (Human) 클래스의 인스턴스를 생성하고, 본인의 이름 변수(ex.seyeon)로 바인딩하시오.
# 3. 사람 (Human) 클래스에 "응애응애"를 출력하는 생성자를 추가하시오.
# 4. 사람(Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하시오.
# 5. 사람(Human) 클래스에 (이름, 나이, 성별)을 출력할 수 있는 printName(), printAge(), printSex() 함수를 추가하시오.
# 6. (2)에서 생성한 인스턴스를 통해 (5)에서 만든 함수에 접근해 각각 이름, 나이, 성별을 출력하시오.

class Human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
        print('응애응애')

    def printName(self):
        print(self.name)
    def printAge(self):
        print(self.age)
    def printSex(self):
        print(self.sex)
    
suhye = Human('수혜', '24', '여자')
suhye.printName()
suhye.printAge()
suhye.printSex()



# 1. 원을 나타내는 Circle이라는 클래스를 생성하시오.
# 2. 원(Circle) 클래스의 인스턴스를 생성하고, circle이라는 변수에 바인딩하시오.
# 3. 원(Circle) 클래스에 반지름(radius), 중심좌표(x, y)를 입력받는 생성자를 추가하시오.
# 4. 원(Circle) 클래스에 원의 넓이를 반환하는 getArea() 함수를 추가하시오.
# -> hint. pi는 math library를 import 하여 사용하시오!
# 5. 원(Circle) 클래스에 원의 중심을 반환하는 getCenter() 함수를 추가하시오.
# 6. (2)에서 생성한 인스턴스에 각각 반지름과 중심좌표를 입력해주는데, 이는 사용자에게 직접 입력 받도록 하시오.
# 7. (4), (5)에서 생성한 함수를 이용해 원의 중심과 중심좌표를 출력하시오.
import math

class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y

    def getArea(self):
        return self.radius*self.radius*math.pi 

    def getCenter(self):
        return self.x, self.y

radius = int(input('원의 반지름: '))
x = int(input('원의 x좌표: '))
y = int(input('원의 y좌표: '))

circle = Circle(radius, x, y)

print('원의 반지름: ', circle.getArea())
print('원의 중심좌표: ', circle.getCenter())