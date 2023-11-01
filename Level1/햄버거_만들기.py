'''
문제 설명
햄버거 가게에서 일을 하는 상수는 햄버거를 포장하는 일을 합니다.
함께 일을 하는 다른 직원들이 햄버거에 들어갈 재료를 조리해 주면 조리된 순서대로 상수의 앞에 아래서부터 위로 쌓이게 되고, 상수는 순서에 맞게 쌓여서 완성된 햄버거를 따로 옮겨 포장을 하게 됩니다.
상수가 일하는 가게는 정해진 순서(아래서부터, 빵 – 야채 – 고기 - 빵)로 쌓인 햄버거만 포장을 합니다.
 상수는 손이 굉장히 빠르기 때문에 상수가 포장하는 동안 속 재료가 추가적으로 들어오는 일은 없으며, 재료의 높이는 무시하여 재료가 높이 쌓여서 일이 힘들어지는 경우는 없습니다.

예를 들어, 상수의 앞에 쌓이는 재료의 순서가 [야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]일 때, 상수는 여섯 번째 재료가 쌓였을 때, 세 번째 재료부터 여섯 번째 재료를 이용하여 햄버거를 포장하고, 아홉 번째 재료가 쌓였을 때, 두 번째 재료와 일곱 번째 재료부터 아홉 번째 재료를 이용하여 햄버거를 포장합니다. 즉, 2개의 햄버거를 포장하게 됩니다.

상수에게 전해지는 재료의 정보를 나타내는 정수 배열 ingredient가 주어졌을 때, 상수가 포장하는 햄버거의 개수를 return 하도록 solution 함수를 완성하시오.

제한사항
1 ≤ ingredient의 길이 ≤ 1,000,000
ingredient의 원소는 1, 2, 3 중 하나의 값이며, 순서대로 빵, 야채, 고기를 의미합니다.
입출력 예
ingredient	result
[2, 1, 1, 2, 3, 1, 2, 3, 1]	2
[1, 3, 2, 1, 2, 1, 3, 1, 2]	0
입출력 예 설명
입출력 예 #1

문제 예시와 같습니다.
입출력 예 #2

상수가 포장할 수 있는 햄버거가 없습니다.

'''

ingredient = [1, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1]  # 2

# count = 0
# left, right = 0, len(ingredient) - 1
# tmp = ''
# while left < right:
#     if ingredient[left] == 1 and ingredient[right] == 1:
#         # 사이에 있는 글자들 더하기
#         for i in range(left+1, right):
#             tmp += str(ingredient[i])
#
#         tmp = tmp.replace('1231', '')
#         if tmp =='23':
#             count += 1
#         tmp = ''
#         left += 1
#         right -= 1
#     elif ingredient[left] == 1:
#         right -= 1
#     elif ingredient[right] == 1:
#         left += 1
#     else:
#         left += 1
#         right -= 1
# print(count)
# 투포인터
def solution(ingredient):
    count = 0
    left, right = 0, len(ingredient) - 1
    tmp = ''
    while left < right:
        if ingredient[left] == 1 and ingredient[right] == 1:
            # 사이에 있는 글자들 더하기
            for i in range(left + 1, right):
                tmp += str(ingredient[i])

            tmp = tmp.replace('1231', '')
            if tmp == '23':
                count += 1
            tmp = ''
            left += 1
            right -= 1
        elif ingredient[left] == 1:
            right -= 1
        elif ingredient[right] == 1:
            left += 1
        else:
            left += 1
            right -= 1
    return count
#
# print(solution(ingredient))

# 그냥 반복문
# count = 0
# tmp = ''.join(map(str, ingredient))
#
# while True:
#     rp = tmp.replace('1231', '', 1)
#     if tmp == rp:
#         break
#     else:
#         tmp = rp
#         count += 1
#
# for i in ingredient:
#     tmp += str(i)
#     while '1231' in tmp:
#         tmp = tmp.replace('1231', '')
#         count += 1
#
count = 0
# tmp = ''.join(map(str, ingredient))
# index = 0
#
# tmp.replace('1231', '', len(tmp)//4)
#
# while index < len(tmp):
#     found = tmp.find('1231', index)
#     if found != -1:
#         tmp = tmp[:found] + tmp[found+4:]
#         count += 1
#         index = max(0, found - 3)
#     else:
#         break
# tmp = ''
# for idx, val in enumerate(ingredient):
ingredient =  [2, 2, 2, 2, 2, 2, 1, 2, 1, 2, 3, 1, 3, 1] # 2


# def solution(ingredient):
#     count = 0
#     i = 0
#     while i < len(ingredient)-3:
#         if ingredient[i:i+4] == [1,2,3,1]:
#             count += 1
#             for _ in range(4):
#                 ingredient.pop(i)
#         else:
#             i += 1
#     return ingredient
# print(solution(ingredient))

# while True:
#     found = False
#     for i in range(len(ingredient) - 3):
#         if ingredient[i:i+4] == [1,2,3,1]:
#             del ingredient[i:i+4]
#             found = True
#             break
#     if not found:
#         break
#
# print(ingredient)


def solution(ingredient):
    count = 0
    i = 0
    result = []
    while i < len(ingredient) - 3:
        if ingredient[i:i+4] == [1,2,3,1]:
            count +=1
            i += 4
        else:
            result.append(ingredient[i])
            i += 1

    return count
print(solution(ingredient))