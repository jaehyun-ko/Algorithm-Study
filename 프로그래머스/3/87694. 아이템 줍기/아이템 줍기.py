from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    # 2배 확장된 맵 사용 (좌표 간 0.5 이동 고려)
    SIZE = 102
    board = [[0] * SIZE for _ in range(SIZE)]

    # 1. 직사각형 내부를 먼저 채운다
    for rect in rectangle:
        x1, y1, x2, y2 = [r * 2 for r in rect]
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                board[i][j] = 1

    # 2. 내부 영역 제거 (외곽만 남김)
    for rect in rectangle:
        x1, y1, x2, y2 = [r * 2 for r in rect]
        for i in range(x1 + 1, x2):
            for j in range(y1 + 1, y2):
                board[i][j] = 0

    # 3. BFS를 위한 시작점, 종료점 세팅
    cx, cy = characterX * 2, characterY * 2
    ix, iy = itemX * 2, itemY * 2
    visited = [[False] * SIZE for _ in range(SIZE)]
    q = deque()
    q.append((cx, cy, 0))
    visited[cx][cy] = True

    # 4방향 탐색
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while q:
        x, y, dist = q.popleft()
        if (x, y) == (ix, iy):
            return dist // 2  # 거리도 2배로 증가했기 때문에 나눠서 반환

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < SIZE and 0 <= ny < SIZE:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, dist + 1))
