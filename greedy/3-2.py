# 큰 수의 법칙
import time


# my solution
def solution1(numbers, m, k):
    start_time = time.time()

    answer = 0
    numbers.sort(reverse=True)
    first = numbers[0]
    second = numbers[1]

    idx = 0
    for _ in range(m): # 8
        idx += 1
        if idx <= k: # 3
            answer += first
        else:
            answer += second
            idx = 0

    print('my solution end time: ', time.time() - start_time)
    return answer


"""
문제 포인트
0. 위와 같이 풀면 간단하기 해결 할 수 있지만, m의 크기가 100억 이상 커진다면 시간 초과 판정을 받을 수도
1. 반복되는 수열에 대해서 파악하는 것이 중요
위의 문제에서 => 6 + 6 + 6 + 5 + 6 + 6 + 6 + 5 이렇게 답을 구함
2. 반복되는 수열은 ? {6, 6, 6, 5}, 반복 되는 수열의 길이는 ? k + 1
3. 반복 횟수 m // (k + 1). 여기에 k를 곱해주면 가장 큰 수가 등장하는 횟수임. 만약 나머지가 있다면 이 부분을 고려하여 더해줘야함 (m % (k + 1))
4. 최종적으로 가장 큰 수가 더해지는 횟수는 ? (m // (k + 1)) * k + (m % (k - 1))
"""


def solution2(numbers, m, k):
    start_time = time.time()

    answer = 0
    numbers.sort(reverse=True)
    first = numbers[0]
    second = numbers[1]

    # 가장 큰 수가 전체 등장 하는 횟수
    count = (m // (k + 1)) * k + (m % (k + 1))

    answer += count * first
    answer += (m - count) * second

    print('book solution end_time: ', time.time() - start_time)
    return answer


if __name__ == '__main__':
    numbers = [2, 4, 5, 4, 6]
    M = 8
    K = 3
    print(solution1(numbers, M, K))
    print(solution2(numbers, M, K))