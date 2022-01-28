def solution(arr):
    arr.sort()

    answer = 0 # total group
    member = 0 # current member
    for i in arr:
        member += 1
        if member >= i:
            member = 0
            answer += 1

    return answer


if __name__ == '__main__':
    arr = [2, 3, 1, 2, 2]
    print(solution(arr))
