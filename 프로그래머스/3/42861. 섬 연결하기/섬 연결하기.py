def solution(n, costs):
    # Union-Find를 위한 parent 배열
    parent = [i for i in range(n)]

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # 경로 압축
        return parent[x]

    def union(a, b):
        root_a = find(a)
        root_b = find(b)
        if root_a != root_b:
            parent[root_b] = root_a
            return True
        return False

    # 비용 기준으로 정렬
    costs.sort(key=lambda x: x[2])

    total_cost = 0
    for a, b, cost in costs:
        if union(a, b):
            total_cost += cost

    return total_cost
