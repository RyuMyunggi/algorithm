# 1로 만들기

def solution(x):
    # + 1을 한 이유는 1번째 수가 인덱스 + 1이기 때
    d = [0] * (x + 1)

    for i in range(2, x + 1):
        d[i] = d[i - 1] + 1
        # 작은 수부터 나누는 이유는 큰 수부터 나누다보면 예외가 발생하는 경우도 발생
        if i % 2 == 0:
            # 혹시 다 나뉘어질 수 있으니 모두 나눠보고 가장 작은 수를 DP 테이블에 저장
            d[i] = min(d[i], d[i // 2] + 1)
        if i % 3 == 0:
            d[i] = min(d[i], d[i // 3] + 1)
        if i % 5 == 0:
            d[i] = min(d[i], d[i // 5] + 1)
        # 작은 문제의 정답을 기록해가면서 큰 문제를 풀어가는 것이 포인트
    return d[x]


if __name__ == '__main__':
    print(solution(7))