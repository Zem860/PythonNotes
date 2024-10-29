# bubblesort排序的例子，取值比較

a = [1, 860, 7, 99 , 2,4,82]

def bubblesort(data):
    list_len = len(data)
    for _ in range(list_len):
        #654321
        for j in range(list_len -1):
            #唯一必須注意的是再python裡面這種必須-1不然j+1會壞掉
            print(j)
            #012345
            if (data[j+1]<data[j]):
                temp = data[j+1]
                data[j+1] = data[j]
                data[j] = temp
    return data
bubblesort(a)

print(bubblesort(a))