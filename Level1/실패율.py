N, stages = 4, [2,2,2,2]

def solution(N, stages):
    # 1단계 포함해서 리트스생성
    fail_list = [[stages.count(1), len(stages)]]

    # 2단계부터 진행 # [[1, 8], [3, 7], [2, 4], [1, 2], [0, 1]]
    for i in range(2, N+1):
        fail_list.append(
            [stages.count(i), (fail_list[i-2][1]-fail_list[i-2][0])])

    # 분수로 표현
    fractions_values = []
    for data in fail_list:
        if data[1] == 0:   # 예외처리 -> 분모가 0 이면 이미 끝난거이므로 그 뒤에는 0을 넣어준다.  
            fractions_values.append(0)
        else:
            fractions_values.append(data[0]/data[1])

    # 원래의 인덱스와 함께 분수 리스트 생성
    indexed_fractions = list(enumerate(fractions_values, 1))

    # 분수값에 따라 내림차순으로 정렬
    sorted_indexed_fractions = sorted(
        indexed_fractions, key=lambda x: x[1], reverse=True)

    # 원래의 순위만 추출
    ranks = [index for index, value in sorted_indexed_fractions]
    return ranks

print(solution(N, stages))