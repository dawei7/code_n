from typing import List

def solve(n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
    # Sort logs by request time
    logs.sort(key=lambda log: log[1])
    
    # Sort queries while keeping track of their original indices
    sorted_queries = sorted(enumerate(queries), key=lambda q: q[1])
    
    ans = [0] * len(queries)
    active_servers = [0] * (n + 1)
    unique_active_count = 0
    
    left_ptr = 0
    right_ptr = 0
    num_logs = len(logs)
    
    for original_idx, q_time in sorted_queries:
        # Expand the window to include logs with time <= q_time
        while right_ptr < num_logs and logs[right_ptr][1] <= q_time:
            server_id = logs[right_ptr][0]
            if active_servers[server_id] == 0:
                unique_active_count += 1
            active_servers[server_id] += 1
            right_ptr += 1
            
        # Shrink the window to exclude logs with time < q_time - x
        while left_ptr < num_logs and logs[left_ptr][1] < q_time - x:
            server_id = logs[left_ptr][0]
            active_servers[server_id] -= 1
            if active_servers[server_id] == 0:
                unique_active_count -= 1
            left_ptr += 1
            
        # The number of servers with zero requests is total servers minus active servers
        ans[original_idx] = n - unique_active_count
        
    return ans
