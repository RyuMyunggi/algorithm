# 시각

def solution(n):
    count = 0
    for i in range(n + 1):
        for j in range(60):
            for k in range(60):
                if '3' in f'{i}:{j}:{k}':
                    count += 1

    return count


if __name__ == '__main__':
    n = 5
    print(solution(n))

# 하나 하나씩 세야 하는 문제. 그런데 아무리 24시간이라고 해도 초로 따지면 86,400 밖에 안됌. 충분함