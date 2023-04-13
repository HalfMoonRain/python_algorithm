# 입력(IP)
# 예제 1
import collections
import re
from typing import Deque


input1 = "A man, a plan, a canal: Panama"
# 출력(OP) : True

# 예제 2
input2 = "race a car"
# 출력 : False

# 풀이 1
"""
pop 을 이용한 풀이
맨앞의 인덱스와 맨 뒤의 값을 비교해서 다르면  False return 
"""
# def isPalindrome(s: str) -> bool:
#     # 전처리 대소문자 구분없이 진행
#     strs = []
#     for char in s:
#         # isalnum : (a-Z, 0-9 인지 확인)
#         if char.isalnum():
#             strs.append(char.lower())

#     # OP: ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']

#     while len(strs) > 1:
#         if strs.pop(0) != strs.pop():
#             return False
#     return True

# 풀이 2
"""
Deque(데크)를 이용한 최적화
--> 속도를 좀 더 높일 수 있다.
자료형을 데크로 선언 하는 것 만으로 풀이1에 비해서 5배정도 속도를 높일 수 있었다. 
리스트구현: O(n^2),
데크 구현 : O(n)
"""


# def isPalindrome(s: str) -> bool:
#     # 전처리 대소문자 구분없이 진행
#     strs: Deque = collections.deque()
#     for char in s:
#         # isalnum : (a-Z, 0-9 인지 확인)
#         if char.isalnum():
#             strs.append(char.lower())

#     # OP: ['a', 'm', 'a', 'n', 'a', 'p', 'l', 'a', 'n', 'a', 'c', 'a', 'n', 'a', 'l', 'p', 'a', 'n', 'a', 'm', 'a']

#     while len(strs) > 1:
#         # deque는 첫 값을 popleft로 꺼내야 한다.
#         if strs.popleft() != strs.pop():
#             return False
#     return True


# 풀이 3
"""
슬라이싱을 이용한 풀이
속도도 가장 빨랐고 코드도 가장 간결해졌다.
정규식을 이용한 언어, 숫자를 걸러 준 뒤 필터링 
슬라이싱의 경우 내부적으로 C로 빠르게 구현되어있어 더 좋은 속도를 기대 할 수 있다.
"""


def isPalindrome(s: str) -> bool:
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)
    return s == s[::-1]


print(isPalindrome(input1))
print(isPalindrome(input2))
