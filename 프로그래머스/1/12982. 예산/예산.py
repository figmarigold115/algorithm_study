def solution(d, budget):
    d.sort()
    cnt = 0
    
    for i in d:
        budget -= i
        if budget < 0:
            return cnt
        cnt += 1
    
    return cnt