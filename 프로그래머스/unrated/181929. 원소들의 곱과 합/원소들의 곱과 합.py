from math import prod

def solution(num_list):
    c1 = prod(num_list)
    c2 = sum(num_list) ** 2
    return 0 if c1>c2 else 1