import itertools
from itertools import combinations
from collections import Counter

"""
포커 승률 계산기. 완전 탐색법을 이용한 버전. 

# 문양
    S: Spade
    D: Diamond
    H: Heart
    C: Clover

# 숫자
    1~10 , J, Q, K, A

# 출력 예시
    당신의 카드를 입력하세요 (예: AS KD): AS KD
    오픈 보드의 3장의 카드를 입력하세요 (예: 10H JS QS): 10H JS QS
    플랍 이후 승률: 56.70%
    당신의 패: 스트레이트
    사용된 카드: ('AS', 'KD', '10H', 'JS', 'QS')
"""

# 포커 핸드 랭킹을 위한 함수
def evaluate_hand(cards):
    ranks = '23456789TJQKA'
    rank_values = {rank: index for index, rank in enumerate(ranks, start=2)}

    # "10" 처리를 위해 모든 카드의 랭크를 올바르게 추출
    card_ranks = []
    for card in cards:
        if card[:-1] == '10':
            card_ranks.append(rank_values['T'])
        else:
            card_ranks.append(rank_values[card[0]])

    card_ranks.sort(reverse=True)
    card_suits = [card[-1] for card in cards]

    is_flush = len(set(card_suits)) == 1
    is_straight = all(card_ranks[i] - card_ranks[i + 1] == 1 for i in range(len(card_ranks) - 1))
    rank_counts = Counter(card_ranks).most_common()

    if is_flush and is_straight and card_ranks[0] == 14:
        return (10, card_ranks)
    elif is_flush and is_straight:
        return (9, card_ranks)
    elif rank_counts[0][1] == 4:
        return (8, rank_counts[0][0], rank_counts[1][0])
    elif rank_counts[0][1] == 3 and rank_counts[1][1] == 2:
        return (7, rank_counts[0][0], rank_counts[1][0])
    elif is_flush:
        return (6, card_ranks)
    elif is_straight:
        return (5, card_ranks)
    elif rank_counts[0][1] == 3:
        return (4, rank_counts[0][0], card_ranks)
    elif rank_counts[0][1] == 2 and rank_counts[1][1] == 2:
        return (3, rank_counts[0][0], rank_counts[1][0], card_ranks)
    elif rank_counts[0][1] == 2:
        return (2, rank_counts[0][0], card_ranks)
    else:
        return (1, card_ranks)


# 핸드 종류를 설명하는 함수
def hand_description(rank):
    descriptions = {
        10: "로열 플러시",
        9: "스트레이트 플러시",
        8: "포카드",
        7: "풀 하우스",
        6: "플러시",
        5: "스트레이트",
        4: "트리플",
        3: "투 페어",
        2: "원 페어",
        1: "하이 카드"
    }
    return descriptions.get(rank[0], "알 수 없는 핸드")


# 가능한 7장의 카드 조합 중 최고의 5장을 찾아 평가하는 함수
def best_hand(cards):
    all_combinations = combinations(cards, 5)
    best = max(all_combinations, key=evaluate_hand)
    return best, evaluate_hand(best)


# 카드 덱 생성
suits = 'H D C S'.split()
ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
deck = [rank + suit for suit, rank in itertools.product(suits, ranks)]


# 사용자로부터 카드 입력 받기
def input_cards(prompt):
    while True:
        try:
            cards = input(prompt).upper().split()
            if all(card in deck for card in cards):
                return cards
            else:
                print("유효하지 않은 카드가 있습니다. 다시 입력해주세요.")
        except ValueError:
            print("올바른 형식으로 카드를 입력해주세요.")


# 덱에서 이미 뽑은 카드를 제거
def remove_cards_from_deck(deck, cards):
    return [card for card in deck if card not in cards]


# 완전 탐색을 사용하여 승률 계산
def exhaustive_enumeration(hand, board, remaining_deck):
    win_count = 0
    tie_count = 0
    loss_count = 0

    for opponent_hand in combinations(remaining_deck, 2):
        for additional_board in combinations([card for card in remaining_deck if card not in opponent_hand],
                                             5 - len(board)):
            full_board = board + list(additional_board)

            my_best_hand = evaluate_hand(hand + full_board)
            opponent_best_hand = evaluate_hand(list(opponent_hand) + full_board)

            if my_best_hand > opponent_best_hand:
                win_count += 1
            elif my_best_hand == opponent_best_hand:
                tie_count += 1
            else:
                loss_count += 1

    total = win_count + tie_count + loss_count
    win_rate = win_count / total
    tie_rate = tie_count / total
    loss_rate = loss_count / total

    return win_rate, tie_rate, loss_rate


# 카드 입력 받기 및 승률 계산
hand = input_cards("당신의 카드를 입력하세요 (예: AS KD): ")
board = []

# 플랍 (첫 3장)
board += input_cards("오픈 보드의 3장의 카드를 입력하세요 (예: 10H JS QS): ")
remaining_deck = remove_cards_from_deck(deck, hand + board)
best_five_cards, best_hand_rank = best_hand(hand + board)
win_rate, tie_rate, loss_rate = exhaustive_enumeration(hand, board, remaining_deck)
print(f"플랍 이후 승률: {win_rate * 100:.2f}%")
print(f"당신의 패: {hand_description(best_hand_rank)}")
print(f"사용된 카드: {best_five_cards}")

# 턴 (4번째 카드)
board += input_cards("턴 카드를 입력하세요 (예: 2D): ")
remaining_deck = remove_cards_from_deck(deck, hand + board)
best_five_cards, best_hand_rank = best_hand(hand + board)
win_rate, tie_rate, loss_rate = exhaustive_enumeration(hand, board, remaining_deck)
print(f"턴 이후 승률: {win_rate * 100:.2f}%")
print(f"당신의 패: {hand_description(best_hand_rank)}")
print(f"사용된 카드: {best_five_cards}")

# 리버 (5번째 카드)
board += input_cards("리버 카드를 입력하세요 (예: 3S): ")
remaining_deck = remove_cards_from_deck(deck, hand + board)
best_five_cards, best_hand_rank = best_hand(hand + board)
win_rate, tie_rate, loss_rate = exhaustive_enumeration(hand, board, remaining_deck)
print(f"리버 이후 승률: {win_rate * 100:.2f}%")
print(f"당신의 패: {hand_description(best_hand_rank)}")
print(f"사용된 카드: {best_five_cards}")