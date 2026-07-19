import bisect

def solve(n: int, queries: list[list[int]]) -> list[int]:
    # We maintain a sorted list of cities that are currently "entry points"
    # to the next segment of the path. Initially, every city i is connected to i+1.
    # The distance is initially n - 1.
    
    # Using a sorted list to keep track of the indices that are currently 
    # part of the shortest path sequence.
    # Initially, the path is 0 -> 1 -> 2 -> ... -> n-1
    active_nodes = list(range(n))
    current_dist = n - 1
    results = []
    
    for u, v in queries:
        # Find the position of u and v in our active nodes list
        idx_u = bisect.bisect_left(active_nodes, u)
        idx_v = bisect.bisect_left(active_nodes, v)
        
        # If u and v are already connected by a shortcut or the path is already 
        # shorter, we check if we need to remove nodes between them.
        # If active_nodes[idx_u] == u and active_nodes[idx_v] == v,
        # then all nodes between idx_u and idx_v are bypassed.
        if idx_u + 1 < idx_v:
            # The number of nodes removed is (idx_v - idx_u - 1)
            nodes_to_remove = idx_v - idx_u - 1
            current_dist -= nodes_to_remove
            # Remove the bypassed nodes from the active list
            del active_nodes[idx_u + 1 : idx_v]
            
        results.append(current_dist)
        
    return results
