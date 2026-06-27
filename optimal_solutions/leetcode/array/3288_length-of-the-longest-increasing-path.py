import bisect

def solve(coordinates: list[list[int]], k: list[int]) -> int:
    kx, ky = k
    
    # Points that can come before k: x < kx and y < ky
    before = [p for p in coordinates if p[0] < kx and p[1] < ky]
    # Sort by x ascending, then y ascending
    before.sort(key=lambda p: (p[0], p[1]))
    
    # Points that can come after k: x > kx and y > ky
    after = [p for p in coordinates if p[0] > kx and p[1] > ky]
    # Sort by x ascending, then y descending
    # This allows us to find LIS on y-coordinates alone
    after.sort(key=lambda p: (p[0], -p[1]))
    
    def get_lis_len(points):
        if not points:
            return 0
        tails = []
        for _, y in points:
            idx = bisect.bisect_left(tails, y)
            if idx < len(tails):
                tails[idx] = y
            else:
                tails.append(y)
        return len(tails)
    
    return 1 + get_lis_len(before) + get_lis_len(after)
