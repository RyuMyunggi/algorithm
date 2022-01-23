# 효율적인 화폐 구성

def solution(numbers, m):
    array = [i for i in range(m + 1)]
    #
    d = [10001] * (m + 1)

    d[0] = 0
    # 각 화폐 단위를 모두 확인
    for i in numbers:
        for j in range(array[i], m + 1):
            if d[j - array[i]] != 10001:
                # 최종 값의 숫자 비교
                # d[j - array[i]]: 현재의 화폐의 단위로 만들 수 있는 바로 전
                # + 1을 하는이유 ? 현재의 값은 전 값에 자기 자신 한 번만 더하면 목표 값이 나옴
                d[j] = min(d[j], d[j - array[i]] + 1)

    if d[m] == 10001:
        return -1
    else:
        return d[m]


if __name__ == '__main__':
    numbers = [2, 3, 5]
    target = 7
    print(solution(numbers, target))


"""
🔑 key
각 화폐 단위인 n을 하나씩 확인하며 최종목표(m)-화폐단위(n)를 만드는 방법이 존재하는지 체크한다.
존재할 경우 해당 화폐 개수에 n화폐를 하나 추가(+1)하면 최종 목표를 이루는 최소 연산 값이 구해진다.

문제 해설: https://www.youtube.com/watch?v=5Lu34WIx2Us
"""



