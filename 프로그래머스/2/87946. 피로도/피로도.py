from itertools import permutations

def solution(k, dungeons):
    answer = -1
    l = len(dungeons)
    per = list(permutations(dungeons, l))

    for p in per:
        cnt = 0
        real = k
        
        for need, use in p:
            if need <= real:
                real -= use
                cnt += 1
                
        answer = max(cnt, answer)
        
    return answer