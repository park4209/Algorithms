import sys
sys.stdin = open("비밀번호_input.txt", "r")
answer = ['0001101', '0011001', '0010011', '0111101', '0100011',\
          '0110001', '0101111', '0111011', '0110111', '0001011']

def findpassword(input_matrix):

    #step1 : password 라인 찾기
    line_ = 0
    for x1 in range(len(input_matrix)):
        if input_matrix[x1].count('1') != 0:
            line_ = x1
    password = input_matrix[line_]

    #step2 : password 시작점 찾기
    x1 = 0
    while x1<M:
        if password[x1:x1+7] in answer:
            password = password[x1:x1+56]
            break
        else:
            x1 += 1

    #step3 : 7자리 씩 자르기
    password2 = []
    for x1 in range(0, len(password), 7):
        password2.append(password[x1:x1+7])

    #step4 : convert password to answer
    password = []
    for x1 in password2:
        password.append(answer.index(x1))

    #step5 : judge correct password
    odd_ = 0
    even_ = 0
    for x1 in range(len(password)-1):
        if x1%2:
            even_ += password[x1]
        else:
            odd_ += password[x1]

    code = (odd_ * 3) + even_ + password[-1]
    if code % 10 == 0:
        return odd_+even_+password[-1]
    else:
        return 0


result = {}
T = int(input())

for case in range(T):
    N, M = map(int, input().split())

    input_matrix = []
    for i in range(N):
        input_matrix.append(input())

    result[case+1] = findpassword(input_matrix)