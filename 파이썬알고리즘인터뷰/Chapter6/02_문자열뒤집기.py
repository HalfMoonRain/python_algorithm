# 문자열을 뒤집는 함수
# 문제 : 문자열을 뒤집는 함수를 작성하라. 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라.
# 예제 1
# 입력
# ['h', 'e', 'l', 'l', 'o']
# 출력
# ['o', 'l', 'l', 'e', 'h']

# 풀이 1 : 투포인터를 이용한 스왑
# def reverseString(s: list[str]) -> None:
#     left, right = 0, len(s) - 1
#     while left < right:
#         s[left], s[right] = s[right], s[left]
#         left += 1
#         right -= 1

# 풀이 2 : 파이썬다운 방식(Pythonic way)
# def reverseString(s: list[str]) -> None:
#    s.reverse()

# 추가 풀이법
# s[:] = s[::-1]
# 이런 트릭은 쉽게 알아내기 어려우며, 문제 발생시 디버깅이 어려워진다.
