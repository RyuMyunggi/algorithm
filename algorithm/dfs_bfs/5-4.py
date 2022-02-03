# 미로 탐색
from collections import deque


def solution(arr, x, y):
    graph = []

    # 기본 이동 방향
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    n = len(arr)
    m = len(arr[0])

    # BFS 소스코드
    queue = deque()
    queue.append((x, y))
    # queue가 빌 때까지 계속
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue
            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른 쪽 부터 최단 거리 반환
    return graph[n - 1][m - 1]


if __name__ == '__main__':
    arr = [
        []
    ]
