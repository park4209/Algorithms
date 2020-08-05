# 정렬 되어있지 않은 경우
def seq_search(a, n, key):
    i = 0
    while i < n and a[i] != key:
        i+=1
    if i < n:
        return i
    else:
        return -1

arr = [4, 9, 11, 23, 2, 19, 7]
key = 233
print(seq_search(arr, len(arr), key))


#정렬 되어 있는 경우
def seq_search2(a, n, key):
    i = 0
    while i < n and a[i] < key:
        i+=1
    if i < n and a[i] ==key:
        return i
    else:
        return -1

arr = [1,2,3,4,5,6,17,18,19]
key = 17
print(seq_search2(arr, len(arr), key))
