def solution(nums):
    
    num = len(nums) // 2
    pkm = len(set(nums))
    
    return num if pkm>num else pkm