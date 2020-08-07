# 선택 정렬
arr = [64, 25, 10, 22, 11, 19, 62, 99, 86, 12, 5, 95]
N = len(arr)



for i in range(10):
    idx = i
    if i % 2 == 0:
        for j in range(i+1, N):
            if arr[idx] < arr[j]:
                idx = j
    else:
        for j in range(i+1, N):
            if arr[idx] > arr[j]:
                idx = j

    arr[i], arr[idx] = arr[idx], arr[i]

print(arr[:10])