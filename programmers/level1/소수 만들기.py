"""
문제 설명
주어진 숫자 중 3개의 수를 더했을 때 소수가 되는 경우의 개수를 구하려고 합니다. 숫자들이 들어있는 배열 nums가 매개변수로 주어질 때, nums에 있는 숫자들 중 서로 다른 3개를 골라 더했을 때 소수가 되는 경우의 개수를 return 하도록 solution 함수를 완성해주세요.

제한사항
nums에 들어있는 숫자의 개수는 3개 이상 50개 이하입니다.
nums의 각 원소는 1 이상 1,000 이하의 자연수이며, 중복된 숫자가 들어있지 않습니다.
입출력 예
nums	result
[1,2,3,4]	1
[1,2,7,6,4]	4
입출력 예 설명
입출력 예 #1
[1,2,4]를 이용해서 7을 만들 수 있습니다.

입출력 예 #2
[1,2,4]를 이용해서 7을 만들 수 있습니다.
[1,4,6]을 이용해서 11을 만들 수 있습니다.
[2,4,7]을 이용해서 13을 만들 수 있습니다.
[4,6,7]을 이용해서 17을 만들 수 있습니다.
"""


# my_solution
def solution1(nums):
    answer = 0
    answers = []
    for i in range(len(nums) - 2):
        num1 = nums[i]
        for j in range(i + 1, len(nums) - 1):
            num2 = nums[j]
            for k in range(j + 1, len(nums)):
                num3 = nums[k]
                num = num1 + num2 + num3
                answers.append(num)

    for num in answers:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            answer += 1
    return answer


# programmers solution
def solution2(nums):
    from itertools import combinations as cb
    """
    key
    : itertools의 조합을 통해 3가지로 만들 수 있는 경우의 수 찾기
    : python for ~ else
    """
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand % j == 0:
                break
        else:
            answer += 1
    return answer


# programmers solution2
from itertools import combinations
def prime_number(x):
    """
    key
    : 소수 판정법 중 주어진 자연수 n에 대해서 1보다 크고 루트 n 이하인 모든 자연수들로 나누어떨어지지 않으면 소수
      **0.5 == 루트
    """
    answer = 0
    for i in range(1, int(x**0.5)+1):
        if x % i == 0:
            answer += 1
    return 1 if answer == 1 else 0

def solution(nums):
    return sum([prime_number(sum(c)) for c in combinations(nums, 3)])


if __name__ == '__main__':
    numbers = [1, 2, 3, 4]
    print(solution1(numbers))