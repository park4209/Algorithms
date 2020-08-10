def find_start(temp_matrix):
    temp = []
    for x in range(N):
        for y in range(N):
            if temp_matrix[x][y] != 0:
                if x == 0:
                    if y == 0:
                        temp.append([x, y])
                    else:
                        if temp_matrix[x][y - 1] == 0:
                            temp.append([x, y])
                else:
                    if y == 0:
                        if temp_matrix[x - 1][y] == 0:
                            temp.append([x, y])
                    else:
                        if temp_matrix[x][y - 1] == 0 and temp_matrix[x - 1][y] == 0:
                            temp.append([x, y])
    return temp

def find_end(start_list):
    temp = []
    for c in start_list:
        x2 = c[0]
        y2 = c[1]

        while x2 < N:
            if temp_matrix[x2][y2] != 0:
                x2 += 1
            else: break
        x2 -= 1

        while y2 < N:
            if temp_matrix[x2][y2] != 0:
                y2 += 1
            else: break
        y2 -= 1

        temp.append([x2, y2])
    return temp

result = []
T = int(input())

for case in range(T):
    N = int(input())

    temp_matrix = []
    for _ in range(N):
        temp_matrix.append(list(map(int, input().split())))

    start_list = find_start(temp_matrix)
    end_list = find_end(start_list)

    area_list = []
    for i in range(len(start_list)):
        h = end_list[i][0] - start_list[i][0] + 1
        w = end_list[i][1] - start_list[i][1] + 1
        area_list.append([h, w, h * w])

    for j1 in range(len(area_list)-1):
        k = j1
        min_area = area_list[j1][2]
        for j2 in range(j1+1, len(area_list)):
            if area_list[j2][2] < min_area:
                min_area = area_list[j2][2]
                k = j2
        area_list[j1], area_list[k] = area_list[k], area_list[j1]

    result.append([case + 1, len(start_list)])

    for res in range(len(area_list)):
        for res2 in range(2):
            result[case].append(area_list[res][res2])

for t in range(len(result)):
    print('#', end='')
    for t1 in range(len(result[t])):
        print(result[t][t1], end=' ')
    print()