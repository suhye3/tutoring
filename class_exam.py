# 아래와 같은 하나의 string을 리스트로 변환해서 출력하세요. 
# -문자열에는 정수, 콤마, 빈칸만 사용할 수 있습니다. 
# -string 내부에는 동일한 숫자를 사용할 수 없습니다.

# 아래의 문제에서는 2가지 문자열을 테스트하세요. 
# 이 문제는 아래를 입력받아서 2번째 가장 큰 값을 출력하는 프로그램을 작성하는 문제입니다. 
# 이를 순서대로 구현하시오.

# - 위의 내용을 함수로 구현하세요. 위의 문제의 입력과 같이 하나의 string을 파라미터로 받아서, 정수 리스트를 반환하는 함수를 작성하시오.
# - 이 함수의 이름은 string_2_list()로 하세요.
# - 이 함수는 list를 반환합니다.

# 위에서 만든 list를 파라미터로 받아서 최대값을 반환하는 함수를 작성하시오.
# - 함수의 이름은 max_of_list()로 하세요.
# - 파이썬의 built-in 함수인 max() 함수를 사용하지 마세요.
# - 이 함수는 int를 반환합니다.

# 위의 max_of_list() 함수를 변경해서 second_max_of_list() 함수를 작성하시오.
# - max() 함수를 사용하지 마세요.
# - 이 함수는 int를 반환합니다.


class Calc: 
    def __init__(self, strInputNum): 
        self.listNum = list(map(int, strInputNum.split(","))) 
 
    def max_of_list(self): 
        nMax = self.listNum[0] 
        for i in self.listNum: 
            if i > nMax: 
                nMax = i 
        return nMax 

    def second_max_of_list(self, bDuplicate = False): 
        arrNew = [] 
        if bDuplicate: 
            arrNew = list(set(self.listNum)) 
        else:
            arrNew = self.listNum
            nFirstMax = nSecondMax = -float("inf") 
            for i in arrNew:
                if i > nFirstMax: 
                    nSecondMax = nFirstMax 
                    nFirstMax = i 
                elif nSecondMax < i < nFirstMax: 
                    nSecondMax = i 
                return nSecondMax 
        
    def second_max_of_list_with_same_numbers(self): 
        return self.second_max_of_list(True) 

inputNum = input("문자열을 입력하세요: ") 
listObj = Calc(inputNum) 
print("first max number: ", listObj.max_of_list()) 
print("second max number: ", listObj.second_max_of_list()) 
print("second max number(중복제거): ", listObj.second_max_of_list_with_same_numbers())
