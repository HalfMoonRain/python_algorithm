"""
포커 승률 계산기. 완전 탐색법을 이용한 버전. 

# 사용법
    1. num_players 설정
    2. 코드실행 후 주어진 행동 실행

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
from itertools import combinations, product
from collections import Counter


# 포커 핸드 랭킹을 위한 함수
def evaluate_hand(cards):
    ranks = '23456789TJQKA'
    rank_values = {rank: index for index, rank in enumerate(ranks, start=2)}

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
deck = [rank + suit for rank, suit in product(ranks, suits)]


# 사용자로부터 카드 입력 받기
def input_cards(prompt, expected_num=2):
    while True:
        try:
            cards = input(prompt).upper().split()
            if len(cards) != expected_num:
                print(f"{expected_num}개의 카드를 입력해야 합니다. 다시 입력해주세요.")
                continue
            if all(card in deck for card in cards):
                return cards
            else:
                print("유효하지 않은 카드가 있습니다. 다시 입력해주세요.")
        except ValueError:
            print("올바른 형식으로 카드를 입력해주세요.")


# 덱에서 이미 뽑은 카드를 제거
def remove_cards_from_deck(deck, cards):
    return [card for card in deck if card not in cards]


# 완전탐색을 사용하여 승률 계산
def exhaustive_enumeration(hand, board, remaining_deck):
    win_count = 0
    tie_count = 0
    loss_count = 0
    strongest_opponent_hand = None
    strongest_opponent_cards = None

    my_best_hand = evaluate_hand(hand + board)

    # 상대방의 가능한 모든 핸드를 탐색
    for opponent_hand in combinations(remaining_deck, 2):
        opponent_best_hand = evaluate_hand(list(opponent_hand) + board)

        if strongest_opponent_hand is None or opponent_best_hand > strongest_opponent_hand:
            strongest_opponent_hand = opponent_best_hand
            strongest_opponent_cards = opponent_hand

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

    return win_rate, tie_rate, loss_rate, strongest_opponent_hand, strongest_opponent_cards


# 플레이어 수 설정 (카드를 덱에서 제거하는 용도로만 사용)
num_players = 5  # 예: 5명의 플레이어

# 카드 입력 받기 및 승률 계산
hand = input_cards("당신의 카드를 입력하세요 (예: AS KD): ", expected_num=2)
deck = remove_cards_from_deck(deck, hand)  # 핸드를 덱에서 제거

board = []

# 플랍 (첫 3장)
board += input_cards("오픈 보드의 3장의 카드를 입력하세요 (예: 10H JS QS): ", expected_num=3)
deck = remove_cards_from_deck(deck, board)  # 보드 카드를 덱에서 제거

# 상대방에게 할당된 카드 수만큼 제거 (플레이어 수를 고려)
deck = deck[:-2 * (num_players - 1)]

best_five_cards, best_hand_rank = best_hand(hand + board)
win_rate, tie_rate, loss_rate, strongest_opponent_hand, strongest_opponent_cards = exhaustive_enumeration(hand, board,
                                                                                                          deck)
print(f"플랍 이후 승률: {win_rate * 100:.2f}%")
print(f"당신의 패: {hand_description(best_hand_rank)}")
print(f"사용된 카드: {best_five_cards}")
print(f"예상되는 가장 강한 상대 패: {hand_description(strongest_opponent_hand)}")
print(f"상대방이 사용한 카드: {strongest_opponent_cards}")

# 턴 (4번째 카드)
board += input_cards("턴 카드를 입력하세요 (예: 2D): ", expected_num=1)
deck = remove_cards_from_deck(deck, board[-1:])  # 새로운 카드를 덱에서 제거

best_five_cards, best_hand_rank = best_hand(hand + board)
win_rate, tie_rate, loss_rate, strongest_opponent_hand, strongest_opponent_cards = exhaustive_enumeration(hand, board,
                                                                                                          deck)
print(f"턴 이후 승률: {win_rate * 100:.2f}%")
print(f"당신의 패: {hand_description(best_hand_rank)}")
print(f"사용된 카드: {best_five_cards}")
print(f"예상되는 가장 강한 상대 패: {hand_description(strongest_opponent_hand)}")
print(f"상대방이 사용한 카드: {strongest_opponent_cards}")

# 리버 (5번째 카드)
board += input_cards("리버 카드를 입력하세요 (예: 3S): ", expected_num=1)
deck = remove_cards_from_deck(deck, board[-1:])  # 새로운 카드를 덱에서 제거

best_five_cards, best_hand_rank = best_hand(hand + board)
win_rate, tie_rate, loss_rate, strongest_opponent_hand, strongest_opponent_cards = exhaustive_enumeration(hand, board, deck)
print(f"리버 이후 승률: {win_rate * 100:.2f}%")
print(f"당신의 패: {hand_description(best_hand_rank)}")
print(f"사용된 카드: {best_five_cards}")
print(f"예상되는 가장 강한 상대 패: {hand_description(strongest_opponent_hand)}")
print(f"상대방이 사용한 카드: {strongest_opponent_cards}")