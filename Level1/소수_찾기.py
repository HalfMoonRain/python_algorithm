'''
문제 설명
1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.

소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
(1은 소수가 아닙니다.)

제한 조건
n은 2이상 1000000이하의 자연수입니다.
입출력 예
n	result
10	4
5	3
입출력 예 설명
입출력 예 #1
1부터 10 사이의 소수는 [2,3,5,7] 4개가 존재하므로 4를 반환

입출력 예 #2
1부터 5 사이의 소수는 [2,3,5] 3개가 존재하므로 3를 반환
'''

n = 5

# primary_number = []
# number = []
# for i in range(2, n+1):
#     number.append(i)
#     if

# 1번풀이. 속도에서 문제가 생김
# def solution(n):
#     count = 0
#     number = list(range(2, n+1))
#     for i in number:
#         if check_primary_number(i):
#             count += 1
#     return count

# def check_primary_number(n:int):
#     divide_range = n//2
#     for i in range(2, divide_range+1):
#         if n % i == 0 :
#             return False
#     return True


# 에라토스테네스의 체
def eratosthenes_sieve(n):
    sieve = [True] * (n+1)  # 처음에는 모든 수를 소수라고 가정합니다. 0부터 n까지의 리스트를 생성합니다.
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아니므로, False로 설정합니다.

    for current_number in range(2, int(n**0.5) + 1):  # n의 제곱근까지만 확인하면 됩니다.
        if sieve[current_number]:  # 현재 수가 소수로 체크되어 있다면
            # 그 수의 배수는 모두 소수가 아닌 것으로 체크합니다.
            for multiple in range(current_number**2, n+1, current_number):
                sieve[multiple] = False

    # True로 남아 있는 수, 즉 소수들을 모아서 반환합니다.
    primes = [num for num in range(2, n+1) if sieve[num]]

    return len(primes)

# 다른 풀이


def solution2(n):
    # 2 ~ n 까지 set을 만듬
    num = set(range(2, n+1))

    # 2부터 값이 있으면 그거보다 큰 배수 들을 지워줌 (에라토스테네스의 체 원리)
    for i in range(2, n+1):
        if i in num:
            # set으로 지워줌.
            num -= set(range(2*i, n+1, i))

    return len(num)

# 활용 풀이


def solution3(n):
    num = set(range(2, n+1))

    for i in range(2, int((n**0.5))+1):
        if i in num:
            num -= set(range(2*i, n+1, i))

    return len(num)


print(solution3(n))
