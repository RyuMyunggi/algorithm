# 선택 정렬

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = array[i]
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = array[j]

    array[i], array[min_index] = array[min_index], array[i]
    # 스와프: 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업
    # 다른 언어도 스와프 함수가 존재하지만 파이썬만큼 간편하지는 않음

print(array)