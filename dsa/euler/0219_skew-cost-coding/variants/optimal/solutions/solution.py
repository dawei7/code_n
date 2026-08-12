def solve(n: int = 10**9) -> int:
    """Find minimum total cost for a prefix-free code of size n with bit costs 0:1, 1:4.
    
    Time Complexity: O(log_phi(n)) where phi is the root of x^4 - x^3 - 1 = 0
    Space Complexity: O(log_phi(n))
    """
    target_n = n
    count = {0: 1}
    curr_n = 1
    total_cost = 0
    curr_min_cost = 0

    while curr_n < target_n:
        while count.get(curr_min_cost, 0) == 0:
            curr_min_cost += 1

        cnt = count[curr_min_cost]
        needed = target_n - curr_n

        if cnt <= needed:
            count[curr_min_cost] = 0
            count[curr_min_cost + 1] = count.get(curr_min_cost + 1, 0) + cnt
            count[curr_min_cost + 4] = count.get(curr_min_cost + 4, 0) + cnt
            total_cost += cnt * (curr_min_cost + 5)
            curr_n += cnt
        else:
            count[curr_min_cost] -= needed
            count[curr_min_cost + 1] = count.get(curr_min_cost + 1, 0) + needed
            count[curr_min_cost + 4] = count.get(curr_min_cost + 4, 0) + needed
            total_cost += needed * (curr_min_cost + 5)
            curr_n += needed
            break

    return total_cost
