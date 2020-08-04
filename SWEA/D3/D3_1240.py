#import sys
#sys.stdin = open("C:\\Users\\Park\\Desktop\\input_1240.txt", "r")
answer = ['0001101', '0011001', '0010011', '0111101', '0100011', \
          '0110001', '0101111', '0111011', '0110111', '0001011']


def findpassword(input_matrix):
    # step1 : password 라인 찾기
    global password2
    x1 = 0
    while x1<=N:
        if input_matrix[x1].count('1') != 0:
            break
        else:
            x1 += 1
    password = input_matrix[x1]

    # step2-3 : password 시작점 찾기 + 정상 password 판별
    x1 = 0
    while x1 < M:
        if password[x1:x1 + 7] in answer:
            password_temp = password[x1:x1 + 56]
            password2 = []
            for x2 in range(0, len(password_temp), 7):
                password2.append(password_temp[x2:x2 + 7])

            while True:
                cnt = 0
                for temp in password2:
                    if temp not in answer:
                        cnt += 1
                break
            if cnt == 0:
                break
            else:
                x1 += 1
        else:
            x1 += 1

    # step4 : convert password to answer
    password = []
    for x1 in password2:
        password.append(answer.index(x1))

    # step5 : judge correct password
    odd_ = 0
    even_ = 0
    for x1 in range(len(password) - 1):
        if x1 % 2:
            even_ += password[x1]
        else:
            odd_ += password[x1]

    code = (odd_ * 3) + even_ + password[-1]
    if code % 10 == 0:
        return sum(password)
    else:
        return 0


result = {}
T = int(input())

for case in range(T):
    N, M = map(int, input().split())

    input_matrix = []
    for i in range(N):
        input_matrix.append(input())

    result[case + 1] = findpassword(input_matrix)


for res in result.keys():
    print(f'#{res} {result[res]}')