"""
문제 설명
3x 마을 사람들은 3을 저주의 숫자라고 생각하기 때문에 3의 배수와 숫자 3을 사용하지 않습니다. 3x 마을 사람들의 숫자는 다음과 같습니다.

10진법	3x 마을에서 쓰는 숫자	10진법	3x 마을에서 쓰는 숫자
1	1	6	8
2	2	7	10
3	4	8	11
4	5	9	14
5	7	10	16
정수 n이 매개변수로 주어질 때, n을 3x 마을에서 사용하는 숫자로 바꿔 return하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ n ≤ 100
입출력 예
n	result
15	25
40	76
입출력 예 설명
입출력 예 #1

15를 3x 마을의 숫자로 변환하면 25입니다.
입출력 예 #2

40을 3x 마을의 숫자로 변환하면 76입니다.
"""
n1 = 15
n2 = 40

"""
이 풀이 방법은 30에서 연속으로 늘려줘야 할 때 처리가 안됨
"""
# def solution(n):

#     i = 1
#     odd_number = 1
#     while i < n:
#         i += 1
#         odd_number += 1
#         if odd_number % 3 == 0:
#             odd_number +=1

#         if '3' in str(odd_number):
#             odd_number += 1
        
#     return odd_number

# print(solution(n2))


""" 
그래서 3을 연속으로 만날 때도 해보았지만 이 경우는 while 문이 이중으로
들어갈 뿐 아니라 오답처리. 테스트 케이스만 통과한다.
"""
# def solution(n):
#     odd_number = 1
#     for i in range(0, n):
#         odd_number += 1
#         if odd_number % 3 == 0:
#             odd_number += 1

#         while '3' in str(odd_number):
#             odd_number += 1
#     return odd_number




# print(solution(n2))

"""
최종
"""
def solution(n):
    count = 1
    curesed_num = 0
    while count <= n:
        curesed_num += 1
        while curesed_num % 3 == 0 or '3' in str(curesed_num):
            curesed_num += 1
        count += 1
    return curesed_num