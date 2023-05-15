'''
### **문제 설명**
정수 배열`numbers`가 매개변수로 주어집니다.
`numbers`의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 
solution 함수를 완성해주세요.
'''

def solution(numbers):
    sortedlist = sorted(numbers)
		# 정렬해서 맨앞 두개와 맨뒤 두개값 곱한 뒤 두수를 비교(둘다 부호가 같을 경우 양의값이 되기 때문)
    return sortedlist[0] * sortedlist[1] if sortedlist[0] * sortedlist[1] > sortedlist[-1] * sortedlist[-2] else sortedlist[-1] * sortedlist[-2]