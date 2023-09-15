a, b, n = 2, 1, 20

'''
돌려 받는 값 -> 몫 * b
연산 후 값 + 나머지(remainder) -> 다음연산값
count = share * b 계속 더해주기
'''
share = 0
remainder = 0
count = 0
while n >= a:
    share = n // a
    remainder = n % a
    count += share * b
    n = share * b + remainder

print(share, remainder, count)
