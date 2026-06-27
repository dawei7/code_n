def solve(points: list[int], m: int) -> int:
    n = len(points)
    
    def check(target: int) -> bool:
        # visits[i] stores how many times we visit index i
        visits = [0] * n
        moves_left = m
        
        # We use a greedy strategy: 
        # To satisfy index i, we can visit i-1, i, or i+1.
        # To be optimal, we prioritize visiting i+1 to help future indices.
        for i in range(n):
            # Current score at i is points[i] * visits[i]
            # Plus points from neighbors: points[i] * visits[i-1] (if i>0)
            # Plus points from neighbors: points[i] * visits[i+1] (if i<n-1)
            
            current_score = points[i] * visits[i]
            if i > 0:
                current_score += points[i] * visits[i-1]
            
            needed = target - current_score
            if needed > 0:
                # We need to add more visits. 
                # We can only add visits to i or i+1.
                # Adding to i+1 is always better for the next index.
                if i == n - 1:
                    # Only option is to visit i
                    needed_visits = (needed + points[i] - 1) // points[i]
                    visits[i] += needed_visits
                else:
                    # Visit i+1 to satisfy i and potentially i+2
                    needed_visits = (needed + points[i] - 1) // points[i]
                    visits[i+1] += needed_visits
            
            # Check if total moves exceed m
            if sum(visits) > m:
                return False
        return sum(visits) <= m

    low = 0
    high = sum(points) * m
    ans = 0
    
    while low <= high:
        mid = (low + high) // 2
        if mid == 0:
            low = mid + 1
            continue
        if check(mid):
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
            
    return ans
