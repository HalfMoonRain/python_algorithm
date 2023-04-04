board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]

# 매직메소드를 이용한 풀이.
def solution(board):
    answer = 0
    boom_list = []
    # 폭탄이 있는 좌표 구하기
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 1:
                boom_list.append([i, j])

    # 폭탄 좌표 주변을 +1 을 해준다
    for x,y in boom_list:
        for i in range(-1, +2):
            for j in range(-1, +2):
                if 0 <= x+i < len(board) and 0 <= y+j < len(board[0]) and (i != 0 or j != 0):
                    board[x+i][y+j] += 1

    # 좌표에서 1이상 갯수 세기
    for i in range(0, len(board)):
        for j in range(0, len(board)):
            if board[i][j] == 0:
                answer += 1

    return answer