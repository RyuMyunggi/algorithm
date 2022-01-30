# 만들 수 없는 금액

def solution(arr):
    arr.sort()
    start = 1
    for i in arr:
        if start >= i:
            start += i
        else:
            break

    return start


if __name__ == '__main__':
    arr = [3, 2, 1, 1, 9]
    print(solution(arr))