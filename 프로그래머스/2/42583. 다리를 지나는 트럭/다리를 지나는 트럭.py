from collections import deque

def solution(bridge_length, weight, truck_weights):
    sec = 0
    bridge_weight = 0
    bridge = deque([0 for _ in range(bridge_length)])
    
    while truck_weights or sum(bridge) > 0:
        bridge_weight -= bridge.popleft()
        if truck_weights and bridge_weight + truck_weights[0] <= weight:
            i = truck_weights.pop(0)
            bridge.append(i)
            bridge_weight += i
        else:
            bridge.append(0)
        sec += 1
    
    return sec