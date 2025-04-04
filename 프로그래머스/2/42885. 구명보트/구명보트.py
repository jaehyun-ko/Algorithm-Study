def solution(people, limit):
    people.sort()  # 몸무게 오름차순 정렬
    left, right = 0, len(people) - 1
    boats = 0

    while left <= right:
        # 두 사람이 함께 탈 수 있다면
        if people[left] + people[right] <= limit:
            left += 1  # 가벼운 사람 태움
        # 무거운 사람은 항상 태움
        right -= 1
        boats += 1

    return boats
