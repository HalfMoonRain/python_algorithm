'''
문제 설명
비밀지도
네오는 평소 프로도가 비상금을 숨겨놓는 장소를 알려줄 비밀지도를 손에 넣었다. 그런데 이 비밀지도는 숫자로 암호화되어 있어 위치를 확인하기 위해서는 암호를 해독해야 한다. 다행히 지도 암호를 해독할 방법을 적어놓은 메모도 함께 발견했다.

지도는 한 변의 길이가 n인 정사각형 배열 형태로, 각 칸은 "공백"(" ") 또는 "벽"("#") 두 종류로 이루어져 있다.
전체 지도는 두 장의 지도를 겹쳐서 얻을 수 있다. 각각 "지도 1"과 "지도 2"라고 하자. 지도 1 또는 지도 2 중 어느 하나라도 벽인 부분은 전체 지도에서도 벽이다. 지도 1과 지도 2에서 모두 공백인 부분은 전체 지도에서도 공백이다.
"지도 1"과 "지도 2"는 각각 정수 배열로 암호화되어 있다.
암호화된 배열은 지도의 각 가로줄에서 벽 부분을 1, 공백 부분을 0으로 부호화했을 때 얻어지는 이진수에 해당하는 값의 배열이다.
secret map

네오가 프로도의 비상금을 손에 넣을 수 있도록, 비밀지도의 암호를 해독하는 작업을 도와줄 프로그램을 작성하라.

입력 형식
입력으로 지도의 한 변 크기 n 과 2개의 정수 배열 arr1, arr2가 들어온다.

1 ≦ n ≦ 16
arr1, arr2는 길이 n인 정수 배열로 주어진다.
정수 배열의 각 원소 x를 이진수로 변환했을 때의 길이는 n 이하이다. 즉, 0 ≦ x ≦ 2n - 1을 만족한다.
출력 형식
원래의 비밀지도를 해독하여 '#', 공백으로 구성된 문자열 배열로 출력하라.

입출력 예제
매개변수	값
n	5
arr1	[9, 20, 28, 18, 11]
arr2	[30, 1, 21, 17, 28]
출력	["#####","# # #", "### #", "# ##", "#####"]
매개변수	값
n	6
arr1	[46, 33, 33 ,22, 31, 50]
arr2	[27 ,56, 19, 14, 14, 10]
출력	["######", "### #", "## ##", " #### ", " #####", "### # "]
'''

# n = 5
# arr = [9, 20, 28, 18, 11]
# bi = []
# for i in arr:
#     bi.append(format(i, 'b').zfill(n))

# print(bi)
n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

a1 = ['101110', '100001', '100001', '010110', '011111', '110010']
a2 = ['011011', '111000', '010011', '001110', '001110', '001010']


def make_list_binary(n, arr):
    bi_list = []
    for i in arr:
        bi_list.append(format(i, 'b').zfill(n))
    return bi_list


def sum_list(n, arr1, arr2):
    sum_list = []
    for i in range(0, len(arr1)):
        sum_list.append(str(int(arr1[i]) + int(arr2[i])).zfill(n))
    return sum_list


def replace_sharp(arr):
    result_list = []
    for i in arr:   # arr = ['12111', '10101', '21201', '20011', '12111']
        tmp_list = []
        for j in list(i):  # list(i) = ['1','2','1','1','1']
            if int(j) > 0:
                tmp_list.append('#')
            elif int(j) == 0:
                tmp_list.append(' ')
        # result_list = ['######', '# # #', '### #', '#  ##', '#####']
        result_list.append(''.join(tmp_list))
    return result_list


def solution(n, arr1, arr2):
    # 각 리스트를 이진수로 표현
    binary_list_1 = make_list_binary(n, arr1)
    binary_list_2 = make_list_binary(n, arr2)

    # 이진수 리스트를 합친다.
    sum = sum_list(n, binary_list_1, binary_list_2)

    # 합친 결과값을 #으로 반환
    return replace_sharp(sum)


print(solution(n, arr1, arr2))

["######", "###  #", "##  ##", "#### ", "#####", "### # "]
["######", "###  #", "##  ##", " #### ", " #####", "### # "]
