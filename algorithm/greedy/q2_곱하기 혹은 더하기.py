def solution(arr):
    answer = 0
    for i in arr:
        number = int(i)
        if answer == 0:
            answer += number
            continue
        if number in [0, 1]:
            answer += number
        else:
            answer *= number

    return answer


if __name__ == '__main__':
    arr = '02984'
    arr = '576'
    arr = '123451821'
    print(solution(arr))