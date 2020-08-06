# 4836. [파이썬 S/W 문제해결 기본] 2일차 - 색칠하기
# 10x10 격자에 빨간색과 파란색을 칠하려고 한다. 두 색깔이 겹쳐서 보라색이 된 칸의 수를 구하라
# ex) 2 2 4 4 1 => (2,2) 부터 (4,4) 까지 1(빨강)로 칠한다

import sys
sys.stdin = open("01.색칠하기_input.txt", "r")

def coloring(mat, com):
    st_x, st_y = com[0], com[1]
    en_x, en_y = com[2], com[3]
    cl = com[4]
    for y in range(st_y, en_y+1):
        for x in range(st_x, en_x+1):
            #같은 색은 다시 칠하지 않는다.
            if mat[x][y] != cl:
                mat[x][y] += cl
    return mat

result = {}
T = int(input())
for case in range(T):

    i_matrix = [0 for _ in range(10)]
    for i in range(10):
        i_matrix[i] = [0 for _ in range(10)]

    N = int(input())
    for _ in range(N):
        command = list(map(int, input().split()))
        i_matrix = coloring(i_matrix, command)

    cnt = 0
    for x in range(10):
        for y in range(10):
            if i_matrix[x][y] >= 3:
                cnt += 1

    result[case+1] = cnt

for res in result.keys():
    print('#{0} {1}'.format(res, result[res]))