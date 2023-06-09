'''
문제 설명
어떤 문장의 각 알파벳을 일정한 거리만큼 밀어서 다른 알파벳으로 바꾸는 암호화 방식을 시저 암호라고 합니다. 예를 들어 "AB"는 1만큼 밀면 "BC"가 되고, 3만큼 밀면 "DE"가 됩니다. "z"는 1만큼 밀면 "a"가 됩니다. 문자열 s와 거리 n을 입력받아 s를 n만큼 민 암호문을 만드는 함수, solution을 완성해 보세요.

제한 조건
공백은 아무리 밀어도 공백입니다.
s는 알파벳 소문자, 대문자, 공백으로만 이루어져 있습니다.
s의 길이는 8000이하입니다.
n은 1 이상, 25이하인 자연수입니다.
입출력 예
s	n	result
"AB"	1	"BC"
"z"	1	"a"
"a B z"	4	"e F d"
'''

s = 'AB'
n = 1
z = 'z'

print(ord('a'))  # 97
print(ord('z'))  # 122
print(ord('A'))  # 65
print(ord('Z'))  # 90
print(ord(' '))  # 32

answer = []
for i in list(s):
    # 소문자
    if 97 <= ord(i) <= 122:
        # n 이 122 넘어갈 수 있으므로
        if ord(i) + n % 122 > 122:
            answer.append(chr(ord(i) + n - 25))
        else:
            answer.append(chr(ord(i) + 1))
    # 대문자 같은 로직
    elif 65 <= ord(i) <= 90:
        if ord(i) + n % 122 > 122:
            answer.append(chr(ord(i) + n - 25))
        else:
            answer.append(chr(ord(i) + 1))

print(answer)


def solution(s, n):
    answer = []
    for i in list(s):
        # 공백 처리
        if i == ' ':
            answer.append(' ')
        # 소문자
        if 97 <= ord(i) <= 122:
            # n 이 122 넘어갈 수 있으므로
            if ord(i) + n > 122:
                answer.append(chr(ord(i) + n - 26))
            else:
                answer.append(chr(ord(i) + n))
        # 대문자 같은 로직
        elif 65 <= ord(i) <= 90:
            if ord(i) + n > 90:
                answer.append(chr(ord(i) + n - 26))
            else:
                answer.append(chr(ord(i) + n))
    return ''.join(answer)


s = 'ZZZ  zzz'
n = 25
print(solution(s, n))
