def solve(side: int, points: list[list[int]], k: int) -> int:
    def get_pos(x, y):
        if y == 0: return x
        if x == side: return side + y
        if y == side: return 2 * side + (side - x)
        return 3 * side + (side - y)

    linear_points = sorted([get_pos(p[0], p[1]) for p in points])
    n = len(linear_points)
    perimeter = 4 * side

    def check(min_dist):
        # Try starting the first point at each possible index
        # To optimize, we only need to check starting points that could be part of an optimal set
        for i in range(n):
            count = 1
            last_pos = linear_points[i]
            curr = i
            
            for _ in range(k - 1):
                # Find next point at least min_dist away
                low = curr + 1
                high = n + i - 1
                next_idx = -1
                
                while low <= high:
                    mid = (low + high) // 2
                    actual_mid = mid % n
                    
                    dist = 0
                    if linear_points[actual_mid] >= last_pos:
                        dist = linear_points[actual_mid] - last_pos
                    else:
                        dist = (perimeter - last_pos) + linear_points[actual_mid]
                    
                    if dist >= min_dist:
                        next_idx = mid
                        high = mid - 1
                    else:
                        low = mid + 1
                
                if next_idx == -1:
                    break
                last_pos = linear_points[next_idx % n]
                curr = next_idx
                count += 1
            
            if count >= k:
                return True
        return False

    low = 0
    high = perimeter // (k - 1) if k > 1 else perimeter
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
