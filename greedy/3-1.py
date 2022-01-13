# 거스름돈

def solution(n, coin_type):
    count = 0

    for coin in coin_type:
        count += n // coin
        n %= coin

    return count


if __name__ == '__main__':
    n = 1260
    coin_type = [500, 100, 50, 10]
    print(solution(n, coin_type))