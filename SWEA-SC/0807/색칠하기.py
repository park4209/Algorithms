# # 빨강 = 1, 파랑 = 2, 보라 = 3
# for tc in range(1, int(input())+1):
#     N = int(input())
#     arr = [[0] * 10 for _ in range(10)]
#
#     for _ in range(N):
#         x1, y1, x2, y2, color = map(int, input().split())
#
#         for i in range(x1, x2+1):
#             for j in range(y1, y2+1):
#                     arr[i][j] += color
#
#     for lst in arr:
#         print(*lst)



arr = [[0]*10 for _ in range(10)]
x, y = 3, 4
size = 5

for i in range(x, x + size):
    for j in range(y, y + size):
        arr[i][j] = 1
for lst in arr:
    print(*lst)