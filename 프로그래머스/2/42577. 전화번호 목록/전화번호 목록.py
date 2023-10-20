def solution(phone_book):
    
    ph = set(phone_book)
    sig = True
    
    for p in ph:
        for i in range(1, len(p)):
            num = p[:-i]
            if num in ph:
                sig = False
                break
    
    return sig