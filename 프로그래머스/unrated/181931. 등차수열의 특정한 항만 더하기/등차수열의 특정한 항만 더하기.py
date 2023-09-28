def solution(a, d, included):
    answer = 0
    for num, i in enumerate(included):
        if i:
            answer += a + d*num
    return answer