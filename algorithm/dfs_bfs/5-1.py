# DFS


def dfs(graph, v, visited):
    # 현재 노드에 대한 방문 처리
    visited[v] = True
    print('v: ', v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        print('i: ', i)
        if not visited[i]:
            print('visited: ', visited)
            dfs(graph, i, visited)


if __name__ == '__main__':
    graph = [
        [],
        [2, 3, 8],
        [1, 7],
        [1, 4, 5],
        [3, 5],
        [3, 4],
        [7],
        [2, 6, 8],
        [1, 7],
    ]

    visited = [False] * 9

    dfs(graph, 1, visited)