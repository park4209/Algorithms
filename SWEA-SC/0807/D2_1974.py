def sudoku_check(test_case):
    # 가로방향 체크
    for i in range(len(test_case)):
        if sorted(test_case[i]) != stand_list:
            return 0

        # 세로방향 체크
        temp_list = []
        for j in range(len(test_case)):
            temp_list.append(test_case[j][i])
        if sorted(temp_list) != stand_list:
            return 0

    # 정사각형 체크
    for w in range(3):
        x1 = 0
        for z in range(3):
            x1 = 0 + 3 * z
            temp_list = []
            for x in range(3):
                y1 = 0 + 3 * w
                for y in range(3):
                    temp_list.append(test_case[x1][y1])
                    y1 += 1
                x1 += 1
            if sorted(temp_list) != stand_list:
                return 0

    return 1


T = int(input())

# 1~9 기준 리스트
stand_list = list(range(1, 10))
result = []

for cases in range(T):

    test_case = []
    for i in range(9):
        temp = list(map(int, input().split()))
        test_case.append(temp)

    result.append(sudoku_check(test_case))

for re in range(len(result)):
    print('#{0} {1}'.format(re+1, result[re]))