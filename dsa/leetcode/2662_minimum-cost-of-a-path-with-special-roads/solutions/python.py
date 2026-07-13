import heapq

def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    """Calculates the Manhattan distance between two points."""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def solve(start: list[int], target: list[int], special_roads: list[list[int]]) -> int:
    """
    Finds the minimum cost to travel from a start point to a target point
    using a combination of normal Manhattan distance travel and special roads.

    Args:
        start: A list [x, y] representing the starting coordinates.
        target: A list [x, y] representing the target coordinates.
        special_roads: A list of lists, where each inner list [x1, y1, x2, y2, cost]
                       describes a special road from (x1, y1) to (x2, y2) with a fixed cost.

    Returns:
        The minimum total cost to reach target from start.
    """
    start_tuple = tuple(start)
    target_tuple = tuple(target)

    # Collect all relevant points that could be intermediate stops or destinations.
    # These include the start, target, and all endpoints of special roads.
    all_points = {start_tuple, target_tuple}
    for sx1, sy1, sx2, sy2, _ in special_roads:
        all_points.add((sx1, sy1))
        all_points.add((sx2, sy2))

    # Initialize distances for all collected points to infinity, except for the start point.
    dist = {point: float('inf') for point in all_points}
    dist[start_tuple] = 0

    # Priority queue stores tuples of (current_cost, point_tuple).
    # It's a min-heap, so the point with the smallest current_cost is always popped first.
    pq = [(0, start_tuple)]

    while pq:
        current_cost, u = heapq.heappop(pq)

        # If we've already found a shorter path to 'u', skip this entry.
        # This can happen because we might add multiple entries for the same node
        # to the priority queue if we find shorter paths to it.
        if current_cost > dist[u]:
            continue

        # If 'u' is the target, we've found the shortest path to it.
        # Since all edge weights are non-negative, this distance is final.
        if u == target_tuple:
            return current_cost

        # Explore paths from 'u':

        # 1. Consider normal Manhattan distance moves to all other relevant points 'v'.
        for v in all_points:
            # A point cannot travel to itself.
            if u == v:
                continue
            
            cost_uv = manhattan_distance(u, v)
            
            # If a shorter path to 'v' is found via 'u', update distance and push to PQ.
            if dist[u] + cost_uv < dist[v]:
                dist[v] = dist[u] + cost_uv
                heapq.heappush(pq, (dist[v], v))

        # 2. Consider special roads starting from 'u'.
        for sx1, sy1, sx2, sy2, scost in special_roads:
            # If the special road starts at our current point 'u'.
            if u == (sx1, sy1):
                v = (sx2, sy2)
                
                # If a shorter path to 'v' is found via this special road from 'u',
                # update distance and push to PQ.
                # 'v' is guaranteed to be in 'all_points' and 'dist' due to initial population.
                if dist[u] + scost < dist[v]:
                    dist[v] = dist[u] + scost
                    heapq.heappush(pq, (dist[v], v))
    
    # If the target was not reachable (should not happen in this problem as Manhattan distance
    # always provides a path), or if the early return was not triggered,
    # return the final distance to the target.
    return dist[target_tuple]
