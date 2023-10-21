from itertools import product

def solution(word):
    answer = 0
    dic = []
    alpha = ['A', 'E', 'I', 'O', 'U']
    
    for i in range(1, 6):
        dic += list(product(alpha, repeat=i))
    
    w = [''.join(map(str, d)) for d in dic]
    w.sort()
    
    return w.index(word)+1