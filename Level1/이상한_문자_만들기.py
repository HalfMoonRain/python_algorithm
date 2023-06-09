'''
문제 설명
문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

제한 사항
문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.
입출력 예
s	return
"try hello world"	"TrY HeLlO WoRlD"
입출력 예 설명
"try hello world"는 세 단어 "try", "hello", "world"로 구성되어 있습니다. 각 단어의 짝수번째 문자를 대문자로, 홀수번째 문자를 소문자로 바꾸면 "TrY", "HeLlO", "WoRlD"입니다. 따라서 "TrY HeLlO WoRlD" 를 리턴합니다.
'''
s = "try hello world"
print(s.split(' '))
answer = ''
for i in s.split(' '):
    for index, val in enumerate(i):
        if index % 2 == 1:
            answer += val.lower()
        elif index % 2 == 0:
            answer += val.upper()
    answer += ' '


def solution(s):
    answer = ''
    # 공백을 기준으로 단어들을 자른다.
    s_list = s.split(' ')
    # 자른 단어들을 기준으로 대소문자 구분한다. 이때 인덱스가 맨 마지막인경우를 제외하면 공백을 추가해준다.
    for idx, i in enumerate(s_list):
        # 공백을 기준으로 나온 단어들의 대소문자 정리
        for index, val in enumerate(i):
            if index % 2 == 1:
                answer += val.lower()
            elif index % 2 == 0:
                answer += val.upper()
        if not idx == (len(s_list)-1):
            answer += ' '
    return answer


print(solution(s))
