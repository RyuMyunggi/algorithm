from collections import defaultdict


def solution(clothes):
    answer = 0

    cloth_dict = defaultdict(int)
    for cloth in clothes:
        cloth_dict[cloth[1]] += 1

    answer += 1
    for key in cloth_dict:
        answer *= (cloth_dict[key] + 1)

    return answer - 1


if __name__ == '__main__':
    clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
    print(solution(clothes))