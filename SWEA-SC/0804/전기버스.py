import sys
sys.stdin = open("전기버스_input.txt", "r")

result = {}
T = int(input())

for case in range(T):
    K, N, M = map(int, input().split())
    M_list = list(map(int, input().split()))

    i = 0
    j = i+K
    cnt = 0
    while i<j and j<N:
        if j in M_list:
            cnt +=1
            i = j
            j = i+K
        else:
            j -= 1
            if j == i:
                cnt = 0

    result[case] = cnt
    
for res in result.keys():
    print('#'+str(res+1), result[res])