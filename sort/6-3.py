# 퀵 정렬


def quick_sort1(array, start, end):
    if start >= end:
        # 퀵 정렬의 종료 조건 (리스트의 원소가 1개) 
        return
    # 호어 분할에 따라 첫번 째 원소가 피벗
    pivot = start 
    left = start + 1
    right = end
    while left <= right: 
        # 피벗보다 큰 데이터를 찾을 때까지 반복 
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 양쪽에서 오다가 엇갈린다면
        if left > right:
            # 피벗과 오른쪽 인덱스를 스와프
            array[right], array[pivot] = array[pivot], array[right] 
        else:
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 정렬 수행
    quick_sort1(array, start, right - 1)
    quick_sort1(array, right + 1, end)

    return array


def quick_sort2(array):
    # 리스트 원소의 수가 1이하면 종료
    if len(array) == 1:
        return array
    
    # pivot 설정
    pivot = array[0]
    # pivot을 제외한 리스트
    tail = array[pivot:]

    # pivot 보다 작은 / 큰 부분 리스트로 정렬
    left_side = [i for i in tail if i < pivot]
    right_side = [j for j in tail if j > pivot]

    return left_side + [pivot] + right_side

if __name__ == '__main__':
    array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
    print(quick_sort1(array, 0, len(array) - 1))
    print(quick_sort2(array))