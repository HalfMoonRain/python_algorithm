"""하노이 탑, 작성자 : JW
원판 더미를 움직이는 퍼즐 게임
"""

import copy
import sys

TOTAL_DISKS = 5  # 원판이 많아질수록 퍼즐은 더 어려워진다

# A 탑에 모든 원판이 놓인 상태로 시작한다.
SOLVED_TOWER = list(range(TOTAL_DISKS, 0, -1))


def main():
    """하노이 탑 게임을 실행한다."""
    print("""하노이 탑, 작성자 JW.
       
    탑에 쌓인 원판을 한 번에 하나씩 다른 탑으로 이동한다. 큰 원판은 작은 원판 위에 놓일 수 없다.
    추가 정보는 https://en.wikipedia.org/wiki/Tower_of_Hanoi를 참고한다.  
    """)

    """
        towers 딕셔너리는 키 “A”, “B”, “C” 와 탑에 쌓인 원판을 표현하는 리스트 형태의 값을 갖고 있다.
        리스트는 다양한 크기의 원판을 표현하는 정수를 포함하며 , 리스트의 시작은 탑의 가장 아래 바닥이다.
        원판 다섯 개로 시작하는 게임의 경우에는 리스트 [5, 4, 3, 2, 1] 가 완성된 탑을 표현한다. 
        리스트 [] 는 탑에 쌓인 원판이 없음을 나타낸다. 리스트 [1, 3] 은 작은 원판 위에큰 원판이 있으며, 유효하지 않은 구성이다. 
        리스트 [3, 1] 이 허용되는 이유는 작은 원판이 큰 원판 상단에 올라갈 수 있기 때문이다.
    """
    towers = {"A": copy.copy(SOLVED_TOWER), "B": [], "C": []}

    while True:  # 이 루프문이 한 번 순회할 때마다 한 턴을 진행한다
        # 탑과 원판을 표시한다
        displayTowers(towers)

        # 사용자에게 이동 명령을 요청한다
        fromTower, toTower = getPlayerMove(towers)

        # 맨 위 원판을 fromTower 에서 toTower 로 이동한다
        disk = towers[fromTower].pop()
        towers[toTower].append(disk)

        # 사용자가 퍼즐을 풀었는지 확인한다
        if SOLVED_TOWER in (towers["B"], towers["C"]):
            displayTowers(towers)
            # 마지막으로 탑을 한 번 더 표시한다
            print(" 퍼즐을 풀었습니다 ! 참 잘했습니다 !")
            sys.exit()


def getPlayerMove(towers):
    """플레이어에게이동명령을요청한다. (fromTower, toTower)를반환한다."""

    while True:  # 플레이어가 유효한 이동 명령을 입력할 때까지 계속 요청한다
        print(' 탑의 " 시작 " 과 " 끝 " 의 글자 또는 QUIT 를 입력하십시오. ')
        print("( 예 : 탑 A 에서 탑 B 로 원판을 이동하려면 AB 를 입력합니다.)")
        print()
        response = input(" > ").upper().strip()

        if response == "QUIT":
            print("즐겁게퍼즐을풀어주셔서감사합니다!")
            sys.exit()

        # 사용자가 유효한 탑 문자를 입력했는지 확인한다
        if response not in ("AB", "AC", "BA", "BC", "CA", "CB"):
            print("AB, AC, BA, BC, CA, CB중하나를입력하십시오.")
            continue  # 플레이어에게 이동 명령을 다시 요청한다.

        # 더 설명적인 변수 이름을 사용한다
        fromTower, toTower = response[0], response[1]

        if len(towers[fromTower]) == 0:
            # from 탑은 비어 있을 수 없다
            print("원판이없는탑을선택했습니다.")
            continue  # 플레이어에게 이동 명령을 다시 요청한다
        elif len(towers[toTower]) == 0:
            # 어떤 원판이라도 빈 “to” 탑으로 이동이 가능하다
            return fromTower, toTower
        elif towers[toTower][-1] < towers[fromTower][-1]:
            print(" 더 작은 원판에 더 큰 원판을 올릴 수 없습니다 . ")
            continue  # 플레이어에게 이동 명령을 다시 요청한다
        else:
            # 유효한 움직임이므로 선택된 탑을 반환한다
            return fromTower, toTower


def displayTowers(towers):
    """세 탑에 배치된 원판을 표시한다 ."""
    # 세 탑을 표시한다
    for level in range(TOTAL_DISKS, -1, -1):
        for tower in (towers["A"], towers["B"], towers["C"]):
            if level >= len(tower):
                displayDisk(0)  # 원판이 없는 빈 기둥을 표시한다
            else:
                displayDisk(tower[level])  # 원판을 표시한다
        print()
    # 탑 이름 A, B, C 를 표시한다
    emptySpace = " " * (TOTAL_DISKS)
    print("{0} A{0}{0} B{0}{0} C\n".format(emptySpace))


def displayDisk(width):
    """ 주어진 width 로 원판을 표시한다 . width 가 0 이면 원판이 없음을 의미한다 ."""
    emptySpace = " " * (TOTAL_DISKS - width)
    if width == 0:
        # 원판이 없는 기둥을 표시한다
        print(f"{emptySpace}||{emptySpace}", end="")
    else:
        # 원판을 표시한다
        disk = "@" * width
        numLabel = str(width).rjust(2, "_")
        print(f"{emptySpace}{disk}{numLabel}{disk}{emptySpace}", end="")


# 이 프로그램이 (임포트되지않고 ) 단독으로 실행되면 , 게임을 시작한다
if __name__ == "__main__":
    main()
