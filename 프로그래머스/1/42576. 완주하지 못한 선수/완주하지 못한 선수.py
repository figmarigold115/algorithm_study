from collections import defaultdict

def solution(participant, completion):
    answer = ''
    
    ptc = defaultdict(int)
    for p in participant:
        ptc[p] += 1
    
    for c in completion:
        if ptc[c] >= 2:
            ptc[c] -= 1
        elif ptc[c] == 1:
            ptc.pop(c)
    
    return list(ptc.keys())[0]