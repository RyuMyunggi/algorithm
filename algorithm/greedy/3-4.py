# 1이 될 떄까지

def solution1(n, k):
    answer = 0

    while True:
        if n == 1:
            break
        if n % k == 0:
            n /= k
        else:
            n -= 1
        answer += 1

    return answer


if __name__ == '__main__':
    number = 25
    k = 3
    print(solution1(number, k))
