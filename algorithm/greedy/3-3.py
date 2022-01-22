# 숫자 카드 게임: 낮은 수 중에서 가장 큰 숫자 찾기
import time


# my solution
def solution1(numbers):
    start_time = time.time()
    answer = 0

    min_values = []
    for number in numbers:
        min_value = min(number)
        min_values.append(min_value)

    answer += max(min_values)

    print('my solution end time: ', time.time() - start_time)
    return answer


# book solution
def solution2(numbers):
    start_time = time.time()
    answer = 0

    for number in numbers:
        min_value = min(number)
        answer = max(answer, min_value)

    print('book solution end time: ', time.time() - start_time)
    return answer


if __name__ == '__main__':
    numbers = [
        [3, 3],
        [3, 10, 3],
        [4, 2, 4],
        [5, 5, 65],
        [435, 12, 56]
    ]
    print(solution1(numbers))
    print(solution2(numbers))