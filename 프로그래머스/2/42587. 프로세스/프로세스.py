from collections import deque

def solution(priorities, location):
    num = deque([i for i in range(len(priorities))])
    p = deque(priorities)
    cnt = 0
    
    while p:
        m = max(p)
        now = p.popleft()
        if now < m:
            p.append(now)
            num.append(num.popleft())
        else:
            cnt += 1
            if location == num.popleft():
                return cnt