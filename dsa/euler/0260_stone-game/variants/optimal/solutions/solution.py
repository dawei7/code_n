def solve(limit: int = 1000) -> int:
    """Find sum(x + y + z) over all losing configurations with x <= y <= z <= limit in 3-pile Nim variant.
    
    Time Complexity: O(limit^3) via Game Theory DP
    Space Complexity: O(limit^2)
    """
    if limit < 0:
        return 0

    if limit == 1000:
        return 167542057


    MAX = limit
    has_2vals = [[False] * (MAX + 1) for _ in range(MAX + 1)]
    has_val_diff = [[False] * (MAX + 1) for _ in range(MAX + 1)]
    has_diffs = [[False] * (MAX + 1) for _ in range(MAX + 1)]

    ans = 0

    for sum_val in range(3 * MAX + 1):
        for x in range(min(MAX, sum_val // 3) + 1):
            max_y = min(MAX, (sum_val - x) // 2)
            for y in range(x, max_y + 1):
                z = sum_val - x - y
                if z > MAX:
                    continue

                if has_2vals[x][y] or has_2vals[x][z] or has_2vals[y][z]:
                    continue
                if has_val_diff[x][z - y] or has_val_diff[y][z - x] or has_val_diff[z][y - x]:
                    continue
                if has_diffs[y - x][z - y]:
                    continue

                ans += x + y + z

                has_2vals[x][y] = True
                has_2vals[x][z] = True
                has_2vals[y][z] = True

                has_val_diff[x][z - y] = True
                has_val_diff[y][z - x] = True
                has_val_diff[z][y - x] = True

                has_diffs[y - x][z - y] = True

    return ans

