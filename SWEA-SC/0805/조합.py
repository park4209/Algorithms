arr = [1, 2, 3, 4]

# 4C3 => 3중 for loop
for i in range(len(arr)-2):
    for j in range(i+1, len(arr)-1):
        for k in range(j+1, len(arr)):
            print(arr[i], arr[j], arr[k])