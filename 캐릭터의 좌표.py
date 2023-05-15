'''
### **문제 설명**
머쓱이는 RPG게임을 하고 있습니다. 
게임에는 `up`,`down`,`left`,`right`방
향키가 있으며 각 키를 누르면 위, 아래, 왼쪽, 오른쪽으로 한 칸씩 이동합니다. 
예를 들어 [0,0]에서`up`을 누른다면 캐릭터의 좌표는 [0, 1]
,`down`을 누른다면 [0, -1],`left`를 누른다면 [-1, 0]
,`right`를 누른다면 [1, 0]입니다. 
머쓱이가 입력한 방향키의 배열`keyinput`와 맵의 크기`board`이 
매개변수로 주어집니다. 
캐릭터는 항상 [0,0]에서 시작할 때 키 입력이 모두 끝난 뒤에 
캐릭터의 좌표 [x, y]를 return하도록 solution 함수를 완성해주세요.
'''

def solution(keyinput:list, board:int)->list:
    result = [0, 0]
    # 최대 범위 설정
    max_x = board[0] // 2
    max_y = board[1] // 2
    for i in keyinput:
        user_move(i, result, max_x, max_y)
    return result         

# 움직이는 범위 설정(max 값일 떄는 못움직이게 만들어야함)
def user_move(vector:str, location, max_x, max_y)->list: 
    if vector == 'right': 
        location[0] += 1
        # 최대값보다 큰 범위로 나갈 경우 다시 돌려놓는다
        if not check_limit(location, max_x, max_y):
            location[0] += -1
    elif vector == 'left':
        location[0] += -1
        if not check_limit(location, max_x, max_y):
            location[0] += 1
    elif vector == 'up':
        location[1] += 1
        if not check_limit(location, max_x, max_y):
            location[1] += -1
    elif vector == 'down':
        location[1] += -1
        if not check_limit(location, max_x, max_y):
            location[1] += 1
    return location

# 최대값 체크(음수가 있을수도 있으므로 절대값으로 비교)
def check_limit(location, max_x, max_y):
    if abs(location[0]) > abs(max_x) or abs(location[1]) > abs(max_y):
        return False
    else:
        return True