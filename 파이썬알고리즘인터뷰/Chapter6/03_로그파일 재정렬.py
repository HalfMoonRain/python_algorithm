'''
문제 : 로그를 재정렬하라. 기준은 다음과 같다.
1. 로그의 가장 앞 부분은 식별자다.
2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
4. 숫자 로그는 입력 순서대로 한다.

ex)
입력:
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
출력:

'''
logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6",
        "let2 own kit dig", "let3 art zero"]
# for log in logs:
#     print(log.split()[1])
# 풀이 1 : 람다와 + 연산자를 이용


def reorderLogFiles(logs: list[str]) -> list[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)
    print("letters", letters)
    print("digits", digits)
    # 2개의 키를 람다 표현식으로 정렬
    # key는 sort할때 기준을 말함
    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    print(letters)
    return letters + digits


print(reorderLogFiles(logs))

# 람다식은 코드를 간결하게 만들 수 있지만 map, filter등과 같이 쓰게 되면 오히려 가독성을 해칠수 있으므로 주의해야한다.
