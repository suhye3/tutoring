# 아래와 같은 하나의 string을 리스트로 변환해서 출력하세요. 문자열에는 정수, 콤마, 빈칸만 사용할
# 수 있습니다. string 내부에는 동일한 숫자를 사용할 수 없습니다.
# 아래의 문제에서는 2가지 문자열을 테스트하세요. 이 문제는 아래를 입력받아서 2번째 가장 큰 값을
# 출력하는 프로그램을 작성하는 문제입니다. 이를 순서대로 구현하시오
str1 = "3, 5, 10, 20, 6, 100, 50, 1"
str2 = "34, 21, 3, 100, 12, 82, 77, 91, 26"
list1 = list(map(int, list(str1.split(', '))))  # 정수로 변환하지 않고 진행 시 문자로 취급하여 정렬이 안될 수 있음
list2 = list(map(int, list(str2.split(', '))))

def sort_list(sortNum):
  sortNum.sort(reverse=True)  # sort = return 값이 없는 함수
  return sortNum[1]

s = sort_list(list1)
print(s)



# - 위의 내용을 함수로 구현하세요. 위의 문제의 입력과 같이 하나의 string을 파라미터로 받아서, 
#   정수 리스트를 반환하는 함수를 작성하시오.
#  - 이 함수의 이름은 string_2_list()로 하세요.
#  - 이 함수는 list를 반환합니다.

def string_2_list(a):
    numa = list(map(int, str1.split(" ")))
    return numa



#  - 위에서 만든 list를 파라미터로 받아서 최대값을 반환하는 함수를 작성하시오.
#     - 함수의 이름은 max_of_list()로 하세요.
#     - 파이썬의 built-in 함수인 max() 함수를 사용하지 마세요.
#     - 이 함수는 int를 반환합니다.
#     - 이 함수를 이용하여, 위의 2개의 string 샘플을 테스트, 출력하시오.

def max_of_list(b):
    nmax = 0
    for i in b:
        if i > nmax:
            nmax = i
    return nmax



# - 위의 max_of_list() 함수를 변경해서 second_max_of_list() 함수를 작성하시오.
# - max() 함수를 사용하지 마세요.
# - 이 함수는 int를 반환합니다.
# - 이 함수를 이용하여, 위의 2개의 string 샘플을 테스트, 출력하시오.

def second_max_of_list(c):
    max_2 = c[0]
    for i in c:
        if i > nmax_2 and i < max_of_list(c):
            nmax_2 = i
    return nmax_2



# 위에서 작성한 함수들을 변경해서 second_max_of_list_with_same_numbers() 함수를 작성하시오.
# 중복된 숫자들은 1개로 정리한 후.
# second_max를 출력해야 합니다.
# 이 함수를 이용하여, 위의 2개의 string 샘플을 테스트, 출력하시오.

sam1 = "3, 5, 10, 100, 3, 50, 1, 20, 6, 100, 50, 1, 50, 100"
sam2 = "34, 91, 3, 12, 5, 91, 3, 100, 12, 82, 77, 91, 26, 12, 3"

sam_list1 = list(map(int, list(sam1.split(', '))))
sam_list2 = list(map(int, list(sam2.split(', '))))

def second_max_of_list_with_same_numbers(f):
  sam_set = list(set(f))
  return second_max_of_list(sam_set)

second_max_of_list_with_same_numbers(sam_list1)



# - 정수 n, m 을 각각 입력받는다.
# - 별(*) 문자를 이용해 가로 길이가 n, 새로의 길이가 m인 직사각형 형태를 출력하시오.
# !! 제한조건 !!
# - n과 m은 각각 1000 이하인 자연수여야 합니다.
# * 입력: 5 3
# * 출력: *****
#         *****
#         *****

n, m = map(int, input().strip().split(' '))

if n >= 1000 and m >=1000:
  pass

for i in range(m):
  for i in range(n):
    print("*", end="")
  print("\n", end="")



# -문자열 s에는 공백으로 구분된 숫자들이 저장되어 있다.
# - str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)" 형태의 문자열을 반환하는 함수, solution을
# 완성하시오.
# - 예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.
# !!! 제한조건 !!!
# - s에는 둘 이상의 정수가 공백으로 구분되어 있다

def solution(s):
    arr = list(map(int, s.strip().split(" ")))
    ansewr = str(min(arr)) + " " + stR(max(arr))
    return ansewr
