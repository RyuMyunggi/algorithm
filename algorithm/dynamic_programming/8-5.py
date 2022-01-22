# 개미전사

def solution(array):
    d = [0] * 100

    d[0] = array[0]
    d[1] = max(array[0], array[1])
    for i in range(2, len(array)):
        d[i] = max(d[i - 1], d[i - 2] + array[i])

    return d[len(array) - 1]


if __name__ == '__main__':
    array = [1, 3, 1, 5]
    # array = [34, 6, 8, 8, 2, 34, 6, 78, 1, 2, 4, 65, 76, 3, 3, 5, 6, 7, 2, 2, 7, 89]
    print(solution(array))