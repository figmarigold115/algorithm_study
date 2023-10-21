from collections import defaultdict

def solution(clothes):
    answer = 1
    cl = defaultdict(list)
    
    for val, key in clothes:
        cl[key].append(val)
        
    for c in cl.values():
        answer *= len(c)+1
    
    return answer-1