def solution(brown, yellow):
    answer = []
    area = brown + yellow
    
    for i in range(1, yellow+1):
        if yellow % i == 0:
            j = yellow // i
            if (i+2) * (j+2) == area:
                answer.append(i+2)
                answer.append(j+2)
                break
                
    answer.sort(reverse=True)
    
    return answer