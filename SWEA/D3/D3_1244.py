# 1244. [S/W 문제해결 응용] 2일차 - 최대 상금
# 최대 6개의 숫자판과 최대 10회의 교환 횟수가 주어진다.
# 주어진 교환 횟수만큼 두 개 숫자판의 위치를 교환하여 최종적으로 얻을 수 있는 가장 큰 수를 구하라.
# 예시> 3 2 8 8 8 (2회) -> 8 2 8 3 8 -> 8 8 8 3 2

# 변수 임의 입력하여 정렬 해보고 -> 함수화 -> 정답에 맞게 코딩

# T = int(input())
#
# for case in range(T):
#     num, k = map(int, input().split())
#
#     # 입력값 리스트화
#     num_list = []
#     while num // 10 != 0:
#         num_list = [num%10] + num_list
#         num = num // 10
#     num_list = [num%10] + num_list

"""
[ 3 2 8 8 8 ] 의 경우

1) 교환 횟수가 1일 경우 
 -> 1번째 수인 3과 5번째 수인 8을 바꿔 
 -> [8 2 8 8 3] 으로 바꾸는 게 최선의 선택이다.

2) 하지만, 교환 횟수가 2일 경우
 -> 1번째 수인 3과 4번째 수인 8을 바꿔
 -> [8 2 8 3 8] 로 바꾸고,
 -> 2번째 수인 2와 5번째 수인 8을 바꿔
 -> [8 8 8 3 2] 로 바꾸는 게 최선의 선택이다.
 
 위의 예시처럼 남아있는 교환 횟수에 따라 숫자 교환의 타겟이 달라질 수 있음을 고려해야한다.
"""

"""
[ 3 2 1 8 8 8 ] 의 경우

1) 교환 횟수가 1일 경우
  -> [8 2 1 8 8 3]
2) 교환 횟수가 2일 경우
  -> [8 2 1 8 3 8]
  -> [8 8 1 8 3 2]
3) 교환 횟수가 3일 경우
  -> [8 2 1 3 8 8]
  -> [8 8 1 3 2 8]
  -> [8 8 8 3 2 1]
"""

T = int(input())


def dfs(num, n, cnt):
    global ans
    if n == cnt:
        num = int(''.join(list(map(str, num))))
        if num > ans:
            ans = num
        return

    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            num[i], num[j] = num[j], num[i]
            dfs(num, n, cnt + 1)
            num[i], num[j] = num[j], num[i]


for tc in range(1, T + 1):
    num, n = input().split()
    ans = 0
    num = list(num)
    n = int(n)

dfs(num, n, 0)
print(f'#{tc} {ans}')