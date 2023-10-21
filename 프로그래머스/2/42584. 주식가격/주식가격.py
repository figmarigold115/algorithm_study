def solution(prices):
    answer = []
    sec = 0
    
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            sec += 1
            if prices[i] <= prices[j]:
                continue
            else:
                break
        answer.append(sec)
        sec = 0
    
    return answer