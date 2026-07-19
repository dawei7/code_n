import heapq

def solve(vals: list[int], edges: list[list[int]], k: int) -> int:
    # Build adjacency list
    adj = [[] for _ in range(len(vals))]
    for u, v in edges:
        adj[u].append(vals[v])
        adj[v].append(vals[u])
    
    max_star_sum = float('-inf')
    
    # For each node, calculate the max star sum if it were the center
    for i in range(len(vals)):
        # Get all neighbor values
        neighbors = adj[i]
        
        # We want the largest k values. 
        # If k is 0, the sum is just the node's own value.
        if k == 0:
            current_sum = vals[i]
        else:
            # Sort neighbors descending to pick the best ones
            neighbors.sort(reverse=True)
            
            # Take up to k neighbors, but only if they are positive
            # (Since we can pick "at most" k, we stop if values become negative)
            current_sum = vals[i]
            for j in range(min(len(neighbors), k)):
                if neighbors[j] > 0:
                    current_sum += neighbors[j]
                else:
                    break
        
        if current_sum > max_star_sum:
            max_star_sum = current_sum
            
    return int(max_star_sum)
