# 4839. [파이썬 S/W 문제해결 기본] 2일차 - 이진탐색
# 책의 총 페이지 수 P
# A와 B가 각각 찾아야할 페이지 Pa, Pb 가 주어질때 누가 더 빨리 찾는지 찾아라
# c = int( (l+r) / 2 )

import sys
sys.stdin = open("03.이진탐색_input.txt", "r")

def bin_search(page, target):
    l = 1
    r = page
    c = int((l+r)/2)
    cnt = 1
    while c!=target:
        if c<target: l = c
        elif c>target: r = c
        cnt += 1
        c = int((l + r) / 2)
    return cnt

T = int(input())
result = {}

for case in range(T):
    P, A, B = map(int, input().split())
    if bin_search(P, A) > bin_search(P, B):
        case_result = 'B'
    elif bin_search(P, A) < bin_search(P, B):
        case_result = 'A'
    else:
        case_result = '0'
    result[case+1] = case_result

for res in result.keys():
    print('#{0} {1}'.format(res, result[res]))