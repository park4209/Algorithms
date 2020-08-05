# def selectionSort(a):
#     # i : 0 ~ len(n) -1
#     for i in range(len(a)-1): #5개 일 때 : 0, 1, 2, 3  (4번)
#         #최소값 찾기
#         min = i
#         for j in range(i+1, len(a)):
#             if a[min] > a[j]:
#                 min = j
#         a[i], a[min] = a[min], a[i]
#
# arr = [64, 25, 10, 22, 11]
# selectionSort(arr)
# print(arr)


def selection(a, k):
    # i : 0 ~ len(n) -1
    for i in range(k):
        # 최소값 찾기
        min = i
        for j in range(i+1, len(a)):
            if a[min] > a[j]:
                min = j
        a[i], a[min] = a[min], a[i]
    return a[k-1]

arr = [64, 25, 10, 22, 11]
print(selection(arr, 2))