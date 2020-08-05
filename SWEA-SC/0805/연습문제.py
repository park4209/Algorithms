"""
<Input>
5
1 1 1 1 1
1 0 0 0 1
1 0 0 0 1
1 0 0 0 1
1 1 1 1 1

[ 순서 ]
1. 인덱스 범위 검사
2. 계산 (절대값)
"""


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

all_sum = 0
for x in range(N):
    for y in range(N):
        temp_sum = 0
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]

            if 0 <= testX < N and 0 <= testY < N:
                temp = arr[testX][testY] - arr[x][y]
                if temp <0 :
                    temp = -temp

                temp_sum += temp
        all_sum  += temp_sum

print(all_sum) #=> 24


