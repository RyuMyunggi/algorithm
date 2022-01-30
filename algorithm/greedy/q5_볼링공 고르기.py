# 볼링공 고르기

def solution1(arr):
    arr.sort()
    count = 0
    for i in range(len(arr) - 1):
        number1 = arr[i]
        for j in range(i + 1, len(arr)):
            number2 = arr[j]
            if number1 != number2:
                count += 1

    return count


def solution2(arr):
    array = [0] * 11
    for x in arr:
        array[x] += 1

    result = 0
    m = max(arr)
    n = len(arr)
    for i in range(1, m + 1):
        n -= array[i]
        result += array[i] * n

    return result


if __name__ == '__main__':
    arr = [1, 3, 2, 3, 2]
    arr = [1, 5, 4, 3, 2, 4, 5, 2]
    print(solution2(arr))