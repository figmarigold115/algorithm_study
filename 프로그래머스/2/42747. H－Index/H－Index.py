def solution(citations):
    answer = 0
    l = len(citations)
    citations.sort(reverse=True)
    
    for i in range(l):
        if citations[i] > i:
            answer += 1
    return answer