# 럭키 스트레이트

def solution(numbers):
    numbers = str(numbers)
    first = numbers[:len(numbers)//2]
    second = numbers[len(numbers)//2:]

    total1, total2 = 0, 0
    for num1, num2 in zip(first, second):
        total1 += int(num1)
        total2 += int(num2)

    if total1 == total2:
        return 'LUCKY'
    return 'READY'


if __name__ == '__main__':
    numbers = 123402
    numbers = 7755
    print(solution(numbers))