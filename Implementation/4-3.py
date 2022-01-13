# 왕실의 나이트

import string


def solution(position, n):
    answer = 0

    alphabet = list(string.ascii_lowercase)
    column = alphabet.index(position[0]) + 1
    row = int(position[1])

    commands = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

    for command in commands:
        next_column = column + command[0]
        next_row = row + command[1]

        if next_column <= n and next_column >= 1 and next_row <= n and next_row >= 1:
            answer += 1

    return answer


if __name__ == '__main__':
    n = 8
    print(solution('c2', n))





