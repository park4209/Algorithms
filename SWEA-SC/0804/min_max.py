import sys
sys.stdin = open("min_max_input.txt", "r")

T = int(input())

result = {}
for case in range(T):
    N = int(input())
    ai = list(map(int, input().split()))

    min_num = ai[0]
    max_num = ai[0]

    for i in range(1, len(ai)):
        if ai[i] < min_num:
            min_num = ai[i]
        elif ai[i] > max_num:
            max_num = ai[i]
            
    result[case] = max_num - min_num

for res in result.keys():
    print('#'+str(res+1), result[res])