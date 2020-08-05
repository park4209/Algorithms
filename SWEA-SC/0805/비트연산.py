# #비트연산자
# a = 5 #0101
# b = 3 #0011
#
# print(a & b)  #0001 , 논리곱
# print(a | b)  #0111 , 논리합
# print(1 << 3) #0001 -> 1000 = 2^3
# print(a ^ b)  #0110


arr = [1, 2, 3]
N = len(arr)

for i in range(1<<N):
    for j in range(N):
        if i & (1<<j):
            print(arr[j], end=" ")
    print()

print(3<<3)