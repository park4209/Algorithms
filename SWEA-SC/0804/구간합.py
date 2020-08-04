import sys
sys.stdin = open("구간합_input.txt", "r")

#sum 함수 사용 X
result = {}
T = int(input())

for case in range(T):
    N, M = map(int, input().split())
    v = list(map(int, input().split()))

    min_num = max_num = sum(v[0:M])
    for i in range(1, (len(v)-M+1)):
        temp_sum = 0
        for j in range(i, i+M):
            temp_sum += v[j]
        if temp_sum > max_num:
            max_num = temp_sum
        elif temp_sum < min_num:
            min_num = temp_sum

    result[case] = max_num - min_num
    
for res in result.keys():
    print('#'+str(res+1), result[res])