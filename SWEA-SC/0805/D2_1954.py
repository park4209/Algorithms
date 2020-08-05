T = int(input())
result = {}
for case in range(T):
    N = int(input())

    #빈 행렬 선언
    mylist = [0 for _ in range(N)]
    for i in range(N):
        mylist[i] = [0 for _ in range(N)]

    # 우 하 좌 상
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    z = 1
    d = 0
    x = 0
    y = 0
    mylist[x][y] = 1
    while z<N**2:
        z += 1
        d1 = d % 4
        if (x+dx[d1] <N) and (y+dy[d1]<N):
            if mylist[x + dx[d1]][y + dy[d1]] == 0:
                x = x + dx[d1]
                y = y + dy[d1]
                mylist[x][y] = z
            else:
                d += 1
                z -= 1
        else:
            d += 1
            z -= 1

    result[case+1] = mylist

for res in result.keys():
    print(f'#{res}')
    for res2 in result[res]:
        for res3 in res2:
            print(res3, end=" ")
        print()