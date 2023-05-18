sides = [3,6]
def solution(sides):
    # 두개의 값이 같은 경우
    if sides[0] == sides[1]:
        return sides[0] * 2 - 1
    
    # 첫번째 값이 젤 큰걸로 고정
    if sides[0] < sides[1]:
        sides[0], sides[1] = sides[1], sides[0]
        return solution(sides)

    # 둘 중 값이 큰 값이 최댓값 일 경우
    #answer = sides[0]-(sides[0] - sides[1] + 1) + 1
    #5 ~ 11
    if sides[0] - sides[1] >= 1:
        answer = sides[1]
    
    # 새로운 값이 값이 최대 일 경우
    # 12 ~ 17 sides[0] + 1,  sides[0] + sides[1]
    
    answer += sides[1] - 1
    return answer

print(solution(sides))