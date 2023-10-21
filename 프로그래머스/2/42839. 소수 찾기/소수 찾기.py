from itertools import permutations

def solution(numbers):
    answer = 0
    num = [n for n in numbers]
    nli = []
    
    for i in range(1, len(num)+1):
        per = list(permutations(num, i))
        for p in per:
            nli.append(int(''.join(p)))
    
    for n in set(nli):
        prime = True
    
        if n < 2:
            continue
        
        for j in range(2, n):
            if n % j == 0:
                prime = False
                break
                
        if prime:
            answer += 1
    
    return answer