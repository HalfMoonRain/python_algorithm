"""
문제 : 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라. 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

입력 :
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
    banned = ["hit"]

출력 :
    "ball"
"""

# 대소문자 뿐만 아니라 쉼표 등 구두점이 존재한다.
# 따라서 데이터 클랜징이라 부르는 입력값에 대한 전처리 작업이 필요하다.
# 정규식을 사용 할 경우 더 편하게 작업을 할 수 있다.
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

'''
정규식에서
\w : 단어 문자
^ : not

re.sub 는 문자 치환.
'''
words = [word for word in re.sub(
    r'[^\w]', ' ', paragraph).lower().split() if word not in banned]


