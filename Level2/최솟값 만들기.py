A, B = [1, 4, 2], [5, 4, 4]

A.sort()
B.sort(reverse=True)
answer = 0
for a, b in zip(A,B):
    answer += a * b
print(answer)