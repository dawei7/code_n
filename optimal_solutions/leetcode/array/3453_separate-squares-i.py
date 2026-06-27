def solve(squares: list[list[int]]) -> float:
    def get_area_below(k: float) -> float:
        total_area = 0.0
        for x, y, l in squares:
            # The square spans [y, y + l]
            # We want the intersection of [y, y + l] and [0, k]
            bottom = y
            top = y + l
            if k > bottom:
                overlap = min(k, top) - bottom
                total_area += overlap * l
        return total_area

    total_sum = sum(l * l for x, y, l in squares)
    target = total_sum / 2.0
    
    low = min(s[1] for s in squares)
    high = max(s[1] + s[2] for s in squares)
    
    # Perform binary search for 100 iterations to ensure high precision
    for _ in range(100):
        mid = (low + high) / 2
        if get_area_below(mid) < target:
            low = mid
        else:
            high = mid
            
    return high
