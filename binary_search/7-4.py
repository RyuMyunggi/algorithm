# 부분 탐색

def solution(array, targets):
    answer = []
    for target in targets:
        is_find = False
        for el in array:
            if el == target:
                is_find = True
                break
        answer.append(is_find)

    return answer


if __name__ == '__main__':
    array = [8, 3, 7, 9, 2]
    targets = [5, 7, 9]
    print(solution(array, targets))