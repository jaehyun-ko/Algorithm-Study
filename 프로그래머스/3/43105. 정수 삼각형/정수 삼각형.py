def solution(triangle):
    # 아래에서부터 위로 올라가면서 계산
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            # 현재 위치에 아래층의 두 자식 중 큰 값을 더함
            triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
    # 꼭대기에 최댓값이 저장되어 있음
    return triangle[0][0]