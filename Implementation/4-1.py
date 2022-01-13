# 상하좌우

def solution(commands, n):
    start = [1, 1]
    commands = [i for i in commands]

    for command in commands:
        if command == 'L':
            if start[1] - 1 < 1:
                continue
            start[1] -= 1
        elif command == 'R':
            if start[1] + 1 > n:
                continue
            start[1] += 1
        elif command == 'U':
            if start[0] - 1 < 1:
                continue
            start[0] -= 1
        else:
            if start[0] + 1 > n:
                continue
            start[0] += 1

    return start



if __name__ == '__main__':
    command = 'RRRUDD'
    n = 5
    print(solution(command, n))