import sys
sys.stdin = open("숫자카드_input.txt", "r")

result = {}
T = int(input())

for case in range(T):
    N = int(input())
    input_data = input()
    
    ai = []
    for i in range(len(input_data)):
        ai.append(input_data[i])
        
    max_num = 0
    max_card = ''
    for i in ai:
        if ai.count(i)> max_num:
            max_num = ai.count(i)
            max_card = i
        elif ai.count(i) == max_num:
            if int(i)>int(max_card):
                max_card = i
            
    result[case] = [int(max_card), ai.count(max_card)]

for res in result.keys():
    print('#'+str(res+1), result[res][0], result[res][1])