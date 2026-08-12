def solve(target_count: int = 12) -> int:
    """Find sum of legs L for the 12 smallest isosceles triangles with h = b +/- 1.
    
    Time Complexity: O(target_count)
    Space Complexity: O(1)
    """
    l_prev, l_curr = 17, 305
    l_sum = l_prev + l_curr

    for _ in range(3, target_count + 1):
        l_next = 18 * l_curr - l_prev
        l_sum += l_next
        l_prev, l_curr = l_curr, l_next

    return l_sum
