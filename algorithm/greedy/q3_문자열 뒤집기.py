def solution(strings):
    count0 = 0
    count1 = 0

    if strings[0] == '1':
        count1 += 1
    else:
        count0 += 1

    # 0 or 1로 변경되는 경우를 확인
    for i in range(len(strings) - 1):
        if strings[i] != strings[i + 1]:
            if strings[i + 1] == '1':
                count0 += 1
            else:
                count1 += 1

    return min(count0, count1)


if __name__ == '__main__':
    strings = '1110011'
    print(solution(strings))