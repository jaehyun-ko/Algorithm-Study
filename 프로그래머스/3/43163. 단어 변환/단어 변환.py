from collections import deque

def can_convert(word1, word2):
    """한 글자만 다른 경우 True 반환"""
    diff = sum([w1 != w2 for w1, w2 in zip(word1, word2)])
    return diff == 1

def solution(begin, target, words):
    if target not in words:
        return 0  # 변환 불가능한 경우

    visited = set()
    queue = deque([(begin, 0)])  # (현재 단어, 변환 단계 수)

    while queue:
        current_word, steps = queue.popleft()
        if current_word == target:
            return steps
        
        for next_word in words:
            if next_word not in visited and can_convert(current_word, next_word):
                visited.add(next_word)
                queue.append((next_word, steps + 1))
    
    return 0  # target까지 도달할 수 없는 경우
