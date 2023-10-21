import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)
    
    while scoville:
        min1 = heapq.heappop(scoville)
        if min1 < K:
            if not scoville:
                return -1
            min2 = heapq.heappop(scoville)
            new = min1 + min2 * 2
            heapq.heappush(scoville, new)
            cnt += 1
        else:
            return cnt