s = "3people  unFollowed me"

answer = ''
s = s.lower()
if s[0].islower():
    answer += s[0].upper()
else:
    answer += s[0]

for i in range(1, len(s)):
    if s[i].islower() and s[i-1] == ' ':
        answer += s[i].upper()
        continue
    answer += s[i]

print(answer)