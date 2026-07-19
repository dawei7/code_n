import heapq

def solve(n: int, k: int, time: list[list[int]]) -> int:
    # Efficiency: left_to_right + right_to_left
    # Priority: Higher efficiency first, then higher index
    # We use negative values for max-heap behavior in Python's min-heap
    
    # left_wait: (-efficiency, -index)
    left_wait = []
    for i in range(k):
        heapq.heappush(left_wait, (-(time[i][0] + time[i][2]), -i))
    
    # right_wait: (-efficiency, -index)
    right_wait = []
    
    # left_busy: (finish_time, index)
    left_busy = []
    # right_busy: (finish_time, index)
    right_busy = []
    
    cur_time = 0
    boxes_left = n
    
    while boxes_left > 0 or right_wait or right_busy:
        # Move workers from busy to wait if they finished their tasks
        while left_busy and left_busy[0][0] <= cur_time:
            _, i = heapq.heappop(left_busy)
            heapq.heappush(left_wait, (-(time[i][0] + time[i][2]), -i))
            
        while right_busy and right_busy[0][0] <= cur_time:
            _, i = heapq.heappop(right_busy)
            heapq.heappush(right_wait, (-(time[i][0] + time[i][2]), -i))
            
        # Try to move someone across the bridge
        if right_wait:
            eff, neg_i = heapq.heappop(right_wait)
            i = -neg_i
            cur_time += time[i][2]
            heapq.heappush(left_busy, (cur_time + time[i][3], i))
        elif boxes_left > 0 and left_wait:
            eff, neg_i = heapq.heappop(left_wait)
            i = -neg_i
            cur_time += time[i][0]
            heapq.heappush(right_busy, (cur_time + time[i][1], i))
            boxes_left -= 1
        else:
            # Jump to the next event
            next_time = float('inf')
            if left_busy: next_time = min(next_time, left_busy[0][0])
            if right_busy: next_time = min(next_time, right_busy[0][0])
            if next_time != float('inf'):
                cur_time = max(cur_time, next_time)
                
    return cur_time
