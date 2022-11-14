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
    return arrNew

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
print("second max number(중복제거): ", 
listObj.second_max_of_list_with_same_numbers())