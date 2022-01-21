"""
< 타겟넘버 >
문제 설명
n개의 음이 아닌 정수가 있습니다. 이 수를 적절히 더하거나 빼서 타겟 넘버를 만들려고 합니다. 예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들려면 다음 다섯 방법을 쓸 수 있습니다.

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3
사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target이 매개변수로 주어질 때 숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 return 하도록 solution 함수를 작성해주세요.

제한사항
주어지는 숫자의 개수는 2개 이상 20개 이하입니다.
각 숫자는 1 이상 50 이하인 자연수입니다.
타겟 넘버는 1 이상 1000 이하인 자연수입니다.
입출력 예
numbers	target	return
[1, 1, 1, 1, 1]	3	5
입출력 예 설명
문제에 나온 예와 같습니다.
"""

# 포인트 ? 최상단 노드에서 아래로 하나씩 들어가 봄  -> 분기는 -거나 +거나 -> 그 다음에 다 연산해봄 -> 목표하는 숫자 나오면 count + 1
from collections import deque
from itertools import product


def solution1(numberes, target):
    super_node = [0]
    for number in numberes:
        sub_node = []
        for node in super_node:
            sub_node.append(node + number)
            sub_node.append(node - number)
        super_node = sub_node
    return super_node.count(target)


def solution2(numbers, target):
    answer = 0
    queue = deque()  # queue 생성

    length = len(numbers)
    queue.append([-numbers[0], 0])
    queue.append([+numbers[0], 0])

    while queue:
        num, i = queue.popleft()
        if i + 1 == length:
            if num == target:
                answer += 1
        else:
            queue.append([num - numbers[i + 1], i + 1])
            queue.append([num + numbers[i + 1], i + 1])

    return answer


def solution3(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)


answer = 0
def dfs(idx, numbers, target, value):
    global answer
    N = len(numbers)

    if(idx== N and target == value):
        answer += 1
        return

    if(idx == N):
        return

    dfs(idx+1, numbers, target, value+numbers[idx])
    dfs(idx+1, numbers, target, value-numbers[idx])


def solution4(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer


# programmers best solution => ...
def solution5(numbers, target):
    if not numbers and target == 0:
        return 1
    elif not numbers:
        return 0
    else:
        return solution5(numbers[1:], target-numbers[0]) + solution5(numbers[1:], target+numbers[0])


if __name__ == '__main__':
    numbers = [1, 7, 1, 2, 1]
    target = 6
    print(solution1(numbers, target))
    print(solution2(numbers, target))
    print(solution3(numbers, target))
    print(solution4(numbers, target))
    print(solution5(numbers, target))