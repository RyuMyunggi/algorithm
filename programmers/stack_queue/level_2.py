
# my solution
def solution(progresses, speeds):
    answer = []
    temp_answers = []
    for i in range(0, len(progresses)):
        progress = progresses[i]
        speed = speeds[i]

        idx = 0
        while True:
            if progress >= 100:
                break
            progress += speed
            idx += 1

        temp_answers.append(idx)

    i = 0
    while True:
        try:
            answer1 = temp_answers[i]
        except:
            break
        count = 1
        while True:
            j = i + 1
            try:
                answer2 = temp_answers[j]
            except:
                answer.append(count)
                i = j
                break
            if answer1 < answer2:
                answer.append(count)
                i = j
                break
            else:
                count += 1
                i += 1

    return answer


# programmers best solution
def solution(progresses, speeds):
    Q = []
    for p, s in zip(progresses, speeds):
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([-((p-100)//s), 1])
        else:
            Q[-1][1] += 1
    return [q[1] for q in Q]


if __name__ == '__main__':
    progresses = [93, 30, 55]
    speeds = [1, 30, 5]
    print(solution(progresses, speeds))