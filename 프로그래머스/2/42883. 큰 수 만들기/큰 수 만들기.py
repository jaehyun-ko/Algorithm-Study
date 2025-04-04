def solution(number, k):
    stack = []
    for digit in number:
        # 큰 숫자를 만들기 위해 이전 숫자를 제거
        while stack and k > 0 and stack[-1] < digit:
            stack.pop()
            k -= 1
        stack.append(digit)
    
    # 아직 k가 남아있다면 뒤에서 제거
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)
