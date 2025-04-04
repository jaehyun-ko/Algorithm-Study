def solution(n, times):
    left = 1
    right = max(times) * n
    answer = right

    while left <= right:
        mid = (left + right) // 2
        people = sum(mid // time for time in times)

        if people >= n:
            answer = mid  # 더 적은 시간으로도 가능한지 확인
            right = mid - 1
        else:
            left = mid + 1

    return answer
