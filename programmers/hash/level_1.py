# my solution
def solution(participants, completions):
    temp = {}
    for participant in participants:
        if temp.get(participant) is None:
            temp[participant] = 0
        temp[participant] += 1

    for completion in completions:
        if temp.get(completion):
            temp[completion] -= 1

    for key in temp:
        value = temp.get(key)
        if value != 0:
            break

    answer = key
    return answer

# programmers best solution
import collections


def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
