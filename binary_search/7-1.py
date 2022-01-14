def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1


if __name__ == '__main__':
    print(sequential_search(5, 2, [5, 1, 4, 2, 1]))
