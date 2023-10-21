def solution(array, commands):
    answer = []
    for s, e, n in commands:
        new = sorted(array[s-1:e])
        answer.append(new[n-1])
    return answer