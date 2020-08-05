#Gravity 예제
data = [7, 4, 2, 0, 0, 6, 0, 7, 0]

N = len(data)

drop_list = []
for i in range(N):
    drop = 0
    cnt = 0
    for j in range(i + 1, N):
        if data[j] >= data[i]:
            cnt += 1
    drop_list.append((N - i) - cnt - 1)

#라인별 최대 낙차
print(drop_list)
#최대 낙차
print(max(drop_list))


"""
for loof를 두개 사용하였기 때문에 효율적인 문제 풀이 방식은 아니다.
"""