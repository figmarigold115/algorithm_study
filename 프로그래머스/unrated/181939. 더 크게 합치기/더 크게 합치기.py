def solution(a, b):
    m = int(''.join(str(a) + str(b)))
    n = int(''.join(str(b) + str(a)))
    return m if m > n else n