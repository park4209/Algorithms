# 4843. [파이썬 S/W 문제해결 기본] 2일차 - 특별한 정렬
# N개의 정수가 주어지면, 가장 큰 수, 가장 작은 수, 2 번째 큰 수, 2 번째 작은 수 .. 순으로 번갈아 정렬한다
# ex) 1 2 3 4 5 6 7 8 9 10 -> 10 1 9 2 8 3 7 4 6 5

import sys
sys.stdin = open("04.특별한정렬_input.txt", "r")

T = int(input())
result = {}

for case in range(T):
    N = int(input())
    input_data = list(map(int, input().split()))

    for i in range(len(input_data)):
        number = input_data[i]
        k = -1
        if i % 2 == 0:
            for j in range(1, len(input_data)-i):
                if number < input_data[i+j]:
                    number = input_data[i+j]
                    k = j
        else:
            for j in range(1, len(input_data)-i):
                if number > input_data[i+j]:
                    number = input_data[i+j]
                    k = j

        if k != -1:
            input_data[i], input_data[i+k] = input_data[i+k], input_data[i]

    result[case+1] = input_data

for res in result.keys():
    print('#{0}'.format(res), end=' ')
    for res2 in result[res][:10]:
        print(res2, end=' ')
    print()