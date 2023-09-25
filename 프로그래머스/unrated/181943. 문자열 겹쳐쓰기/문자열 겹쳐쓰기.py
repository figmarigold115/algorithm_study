def solution(my_string, overwrite_string, s):
    answer = ''
    counter = 0
    
    for i, m in enumerate(my_string):
        if i >= s and counter != len(overwrite_string):
            answer += overwrite_string[counter]
            counter += 1
        else:
            answer += m
            
    return answer