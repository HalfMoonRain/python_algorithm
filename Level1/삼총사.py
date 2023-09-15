'''
문제 설명
한국중학교에 다니는 학생들은 각자 정수 번호를 갖고 있습니다. 이 학교 학생 3명의 정수 번호를 더했을 때 0이 되면 3명의 학생은 삼총사라고 합니다. 예를 들어, 5명의 학생이 있고, 각각의 정수 번호가 순서대로 -2, 3, 0, 2, -5일 때, 첫 번째, 세 번째, 네 번째 학생의 정수 번호를 더하면 0이므로 세 학생은 삼총사입니다. 또한, 두 번째, 네 번째, 다섯 번째 학생의 정수 번호를 더해도 0이므로 세 학생도 삼총사입니다. 따라서 이 경우 한국중학교에서는 두 가지 방법으로 삼총사를 만들 수 있습니다.

한국중학교 학생들의 번호를 나타내는 정수 배열 number가 매개변수로 주어질 때, 학생들 중 삼총사를 만들 수 있는 방법의 수를 return 하도록 solution 함수를 완성하세요.

제한사항
3 ≤ number의 길이 ≤ 13
-1,000 ≤ number의 각 원소 ≤ 1,000
서로 다른 학생의 정수 번호가 같을 수 있습니다.
입출력 예
number	result
[-2, 3, 0, 2, -5]	2
[-3, -2, -1, 0, 1, 2, 3]	5
[-1, 1, -1, 1]	0
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.
입출력 예 #2

학생들의 정수 번호 쌍 (-3, 0, 3), (-2, 0, 2), (-1, 0, 1), (-2, -1, 3), (-3, 1, 2) 이 삼총사가 될 수 있으므로, 5를 return 합니다.
입출력 예 #3

삼총사가 될 수 있는 방법이 없습니다.
'''
numbers = [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0]
# # 브루트 포스
# '''
# 모든 경우의 수를 전부 조회한다. 3중 for문으로 3개를 모두 움직임
# '''
# def brute_force(number: list):
#     results = []
#     number.sort()
#
#     # 브루트 포스 n^3 반복
#     for i in range(len(number) - 2):
#         # 중복 된 값 건너 뛰기
#         if i > 0 and number[i] == number[i - 1]:
#             continue
#         for j in range(i + i, len(number) - 1):
#             #  중복 된 값 건너 뛰기
#             if j > i + 1 and number[j] == number[j - 1]:
#                 continue
#             for k in range(j + 1, len(number)):
#                 #  중복 된 값 건너 뛰기
#                 if k > j + 1 and number[k] == number[k - 1]:
#                     continue
#                 if number[i] + number[j] + number[k] == 0:
#                     results.append((number[i], number[j], number[k]))
#     return results
#
#
# # 문제에 맞게 풀이 변경
# def solution(number):
#     results = 0
#     number.sort()
#
#     # 브루트 포스 n^3 반복
#     for i in range(len(number) - 2):
#         # 중복 된 값 건너 뛰기
#         if i > 0 and number[i] == number[i - 1]:
#             continue
#         for j in range(i + i, len(number) - 1):
#             #  중복 된 값 건너 뛰기
#             if j > i + 1 and number[j] == number[j - 1]:
#                 continue
#             for k in range(j + 1, len(number)):
#                 #  중복 된 값 건너 뛰기
#                 if k > j + 1 and number[k] == number[k - 1]:
#                     continue
#                 if number[i] + number[j] + number[k] == 0:
#                     results += 1
#     return results
#
#
# # 투 포인터
# '''
# 하나를 고정하여 2개의 포인터만 움직인다. 결과값에 따라 포인터를 움직이는 방향이 다르므로 조회 되는 수를 줄일 수 있다.
# '''
# def two_pointer(number):
#     results = []
#     number.sort()
#
#     for i in range(len(number) - 2):
#         # 중복 된 값 건너 뛰기
#         if i > 0 and number[i] == number[i - 1]:
#             continue
#
#         # 간격을 좁혀가며 합 sum 계산
#         left, right = i + 1, len(number) - 1
#         while left < right:
#             sum = number[i] + number[left] + number[right]
#             if sum < 0:
#                 left += 1
#             elif sum > 0:
#                 right -= 1
#             else:
#                 # sum = 0 인 경우이므로 정답 및 스킵 처리
#                 results.append((number[i], number[left], number[right]))
#
#                 while left < right and number[left] == number[left + 1]:
#                     left += 1
#                 while left < right and number[right] == number[right - 1]:
#                     right -= 1
#
#                 left += 1
#                 right -= 1
#     return results
#

def solution(number):
    results = 0
    number.sort()

    for i in range(len(number) - 2):
        # # 중복 된 값 건너 뛰기
        # if i > 0 and number[i] == number[i - 1]:
        #     continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = i + 1, len(number) - 1
        while left < right:
            sum = number[i] + number[left] + number[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                # sum = 0 인 경우이므로 정답 및 스킵 처리
                results += 1

                while left < right and number[left] == number[left + 1]:
                    left += 1
                while left < right and number[right] == number[right - 1]:
                    right -= 1

                left += 1
                right -= 1
    return results

print(solution(numbers))