# 피보나치 수열 메모지에이션

d = [0] * 100


def fibo(x):
    print(f'f({x})')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]

    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]


"""
위와 같은 방식을 메모이제이션이라고함
메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중 한 종류로, 한 번 구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법
메모이제이션은 탑 바운 방식에 국한되어 사용되는 표현. 메모이제이션은 때에 따라서 다른 자료형 예를 들어 dictionary 자료형을 이용할 수 있음. 연속되지 않은 경우에 유용
다이나믹 프로그래밍을 재귀적으로 수행하다가 같은 정보가필요할 때는 이미구현한 정답을 그대로 가져오면 됌
이를 통해 알 수 있는 것은 다이나믹 프로그래밍이란 큰 문제를 작게나누고 같은 문제라면 한 번씩만 풀어 문제를 효율적으로 해결하는 알고리즘
다이나믹 프로그래밍을 적용했을 때 피보나치 수열의 알고리즘의 시간 복잡도는 O(N)
이와 같은이 큰 문제를 해결하기 위해 작은 문제를 호출 한다고 하여 탑 다운 방식이라고함
"""

if __name__ == '__main__':
    print(fibo(6))
