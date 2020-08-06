# 4837. [파이썬 S/W 문제해결 기본] 2일차 - 부분집합의 합
# 1부터 12까지의 숫자를 원소로 갖는 집합 A
# A의 부분 집합 중, N개의 원소를 갖고 있고, 원소의 합이 K인 부분집합의 수
# ex) N = 3, K = 6 인 경우는 {1,2,3} 1 가지만 존재한다

import sys
sys.stdin = open("02.부분집합의합_input.txt", "r")

T = int(input())
A = list(range(1,13))
result = {}
for case in range(T):
    N, K = map(int, input().split())
    cnt_result = 0
    for i in range(1, 1<<len(A)):
        sum_ = 0
        cnt_ = 0
        for j in range(len(A)):
            if i & 1<<j:
                sum_ += A[j]
                cnt_ += 1

        if (sum_ == K) and (cnt_==N):
            cnt_result += 1
    result[case+1] = cnt_result

for res in result.keys():
    print('#{0} {1}'.format(res, result[res]))
