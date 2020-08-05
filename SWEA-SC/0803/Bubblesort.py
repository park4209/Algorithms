def Bubblesort(a):
    i = 1
    for i in range(len(a)-1, 0, -1) : # 4 3 2 1
        for j in range(0, i):
            i+=1
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j] #Swap
                
data = [ 55, 7, 78, 12, 42 ]
Bubblesort(data)
#print(data)
print(data)