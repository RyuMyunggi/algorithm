# 삽입 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1): 
        # i 부터 -1까지 감소하며 반복 
        if array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            # 왼쪽보다 작으면 자리 바꿈
        else:
            # 본인 보다 작은 요소 만나면 break 
            break

print(array) 