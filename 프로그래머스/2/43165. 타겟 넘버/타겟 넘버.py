from itertools import product
def solution(numbers, target):
    l = [(x, -x) for x in numbers]
    s = list(map(sum, product(*l)))
    return s.count(target)

def solution(numbers, target):
    answer = 0

    def dfs(index, current_sum):
        nonlocal answer
        # 모든 숫자를 다 사용했을 때
        if index == len(numbers):
            if current_sum == target:
                answer += 1
            return
        # 현재 숫자를 더하거나 빼기
        dfs(index + 1, current_sum + numbers[index])
        dfs(index + 1, current_sum - numbers[index])
    
    dfs(0, 0)
    return answer