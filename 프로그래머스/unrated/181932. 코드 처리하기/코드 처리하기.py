def solution(code):
    answer = ''
    mode = 0
    
    for i in range(len(code)):
        if code[i] == '1':
            if mode == 0:
                mode = 1
            elif mode == 1:
                mode = 0
        else:
            if mode == 0 and i % 2 == 0:
                answer += code[i]
            elif mode == 1 and i % 2 == 1:
                answer += code[i]
            else:
                continue
                
    if not answer:
        answer = "EMPTY"
                
    return answer