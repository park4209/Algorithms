def Counting_Sort(A, B, k):
    # A [] - 입력 배열 (1 to k)
    # B [] - 정렬된 배열
    # C [] - 카운트 배열

    C=[0] * k

    # A의 값 카운트
    for i in range (0, len(B)):
        C[A[i]] += 1

    # C 배열 값 누적
    for i in range (1, len(C)):
        C[i] += C[i-1]

    # 소트
    for i in range (len(B)-1, -1, -1):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

a = [0, 4, 1, 3, 1, 2, 4, 1] # Source
b = [0] * len(a)

Counting_Sort(a, b, 10)

print(a)
print(b)