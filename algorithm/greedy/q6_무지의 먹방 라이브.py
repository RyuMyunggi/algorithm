# 무지의 먹방 라이브


def solution(food_times, k):
    import heapq
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # 음식 시간, 음식번호 형태로 우선선위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

    # 먹기 위해 사용한 시간
    sum_value = 0
    # 직전에 다 먹은 음식 시간
    previous = 0
    # 남은 음식의 개수
    length = len(food_times)

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1
        previous = now                          # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번 째 음식인지 확인하여 출력
    result = sorted(q, key=lambda el: el[1])    # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]


if __name__ == '__main__':
    foods_times = [3, 1, 2]
    foods_times = [8, 6, 4]
    k = 15
    print(solution(foods_times, k))
