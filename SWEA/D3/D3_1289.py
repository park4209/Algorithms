# 1289. 원재의 메모리 복구하기
# 초기화된 메모리를 원상복구 하는데 몇 번 고쳐야 하는지 구하자
# 단, i번째 bit를 바꾸면 그 이후는 모두 바뀐다 (0000 에서 두번째 bit를 바꾸면 0111 로 바뀜)

T = int(input())
result = {}

for case in range(T):
    input_data = input()
    # 첫번째 비트가 1일 경우 카운팅 해주기 위해 앞에 '0' 을 붙인다
    bit_list = ['0']
    for i in range(len(input_data)):
        bit_list.append(input_data[i])

    cnt = 0
    for j in range(len(bit_list)-1):
        if bit_list[j] != bit_list[j+1]:
            cnt += 1
    result[case+1] = cnt

for res in result.keys():
    print('#{0} {1}'.format(res, result[res]))
