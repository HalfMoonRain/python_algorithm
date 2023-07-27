'''
문제 설명
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

제한사항
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
입출력 예
participant	completion	return
["leo", "kiki", "eden"]	["eden", "kiki"]	"leo"
["marina", "josipa", "nikola", "vinko", "filipa"]	["josipa", "filipa", "marina", "nikola"]	"vinko"
["mislav", "stanko", "mislav", "ana"]	["stanko", "ana", "mislav"]	"mislav"
입출력 예 설명
예제 #1
"leo"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #2
"vinko"는 참여자 명단에는 있지만, 완주자 명단에는 없기 때문에 완주하지 못했습니다.

예제 #3
"mislav"는 참여자 명단에는 두 명이 있지만, 완주자 명단에는 한 명밖에 없기 때문에 한명은 완주하지 못했습니다.
'''
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]


# 리스트에서 동일한 항목을 제거하는 방법 -> 시간 초과
# def solution(participant, completion):
#     for i in completion:
#         participant.remove(i)
#     return participant[0]
# print(solution(participant, completion))

# 시간 초과 하나의 리스트에서만 셀 필요가 있어보임
for i in participant:
    if participant.count(i) > completion.count(i):
        print(i)

# 중복에 적용이 안됨
# print(list(set(participant) - set(completion)))

def solution(participant, completion):
    # dict으로 key, value 로 작업
    runner_dict = {}
    # 참가자 수 만큼 + 1 (중복이름 까지 처리)
    for runner in participant:
        if runner in runner_dict:
            runner_dict[runner] += 1
        else:
            runner_dict[runner] = 1
    
    # 완주자가 생긴 만큼 -1
    for runner in completion:
        if runner in runner_dict:
            runner_dict[runner] -= 1

    # 최종적으로 남는 사람은 +1 이 되있을것이다.
    for runner in runner_dict:
        if runner_dict[runner] > 0:
            return runner
        
'''
차이가 생겼던 이유
리스트로 처리 할 경우 O(n) * O(n) 으로 결과적으로 O(n^2)가 되버려서 상당한 시간이 걸려버렸지만
다음과같이 dict으로 할 경우 for 문을 3번쓰긴하지만 O(n) 이 되므로 시간차이가 데이터가 커질수록 차이가 더 심해진다. 
'''