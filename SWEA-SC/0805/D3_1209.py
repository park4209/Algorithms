result = []
for case in range(10):
    case_result = []
    N = 100
    caseNo = int(input())

    input_matrix = []
    for i in range(N):
        input_line = list(map(int, input().split()))
        input_matrix.append(input_line)

    # 가로방향
    for x1 in range(N):
        case_result.append(sum(input_matrix[x1]))

    # 세로방향
    for x1 in range(N):
        temp_list = []
        for x2 in range(N):
            temp_list.append(input_matrix[x2][x1])
        case_result.append(sum(temp_list))

    # 우하향 대각선
    x = 0
    y = 0
    temp_list = []
    for z in range(N):
        temp_list.append(input_matrix[x][y])
        x += 1
        y += 1
    case_result.append(sum(temp_list))

    # 좌하향 대각선
    x = 0
    y = N - 1
    temp_list = []
    for z in range(N):
        temp_list.append(input_matrix[x][y])
        x += 1
        y -= 1
    case_result.append(sum(temp_list))

    result.append(max(case_result))

for res in range(len(result)):
    print(f'#{res + 1} {result[res]}')