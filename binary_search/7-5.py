# 떡볶이 떡 만들기

def solution(target, array):
    answer = 0
    start = 0
    end = max(array)
    while start <= end:
        total = 0
        # 절단기의 높이
        mid = (start + end) // 2
        for x in array:
            if x > mid:
                # 떡 - 절단기
                total += x - mid

        if total < target:
            end = mid - 1
        else:
            answer = mid
            start = mid + 1

    return answer


if __name__ == '__main__':
    array = [19, 15, 10, 17]
    m = 6
    print(solution(m, array))