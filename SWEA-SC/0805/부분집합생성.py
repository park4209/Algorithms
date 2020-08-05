# 3개의 원소를 갖는 집합의 부분집합 구하기 (2의 3제곱)
# power set
def printList(arr, bit):
    for i in range(len(bit)):
        if bit[i]:
            print(arr[i], end=" ")
    print()


arr = [1, 2, 3]
bit = [0, 0, 0]

for x1 in range(2):
    bit[0] = x1
    for x2 in range(2):
        bit[1] = x2
        for x3 in range(2):
            bit[2] = x3
            printList(arr, bit)
