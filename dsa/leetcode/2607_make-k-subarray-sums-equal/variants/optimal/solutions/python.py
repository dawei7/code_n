import math

def solve(arr: list[int], k: int) -> int:
    n = len(arr)
    k = math.gcd(k, n)
    visited = [False] * n
    total_ops = 0
    
    for i in range(n):
        if not visited[i]:
            # Extract all elements belonging to the same cycle
            cycle = []
            curr = i
            while not visited[curr]:
                visited[curr] = True
                cycle.append(arr[curr])
                curr = (curr + k) % n
            
            # To minimize sum of absolute differences, 
            # we transform all elements in the cycle to their median.
            cycle.sort()
            median = cycle[len(cycle) // 2]
            
            for val in cycle:
                total_ops += abs(val - median)
                
    return total_ops
