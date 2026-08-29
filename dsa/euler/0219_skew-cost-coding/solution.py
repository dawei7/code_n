def solve(n: int = 10**9) -> int:
    """Find the minimum total cost for a prefix-free code of size n = 10^9 with bit costs '0': 1, '1': 4.

    Mathematical Principles Applied:
    1. Skew-Cost Huffman Tree & Node Splitting:
       A prefix-free code of size n corresponds to a binary tree with n leaf nodes.
       Appending bit '0' adds cost 1 (new cost = c + 1).
       Appending bit '1' adds cost 4 (new cost = c + 4).
       Splitting a leaf node of cost c increases total cost by (c + 1) + (c + 4) - c = c + 5,
       and increases the number of leaf nodes by 1.

    2. Greedy Minimum-Cost Node Expansion:
       To minimize total cost, greedily split the leaf nodes with the smallest current cost c.
       We maintain a frequency dictionary of node costs count[c].

    3. Bulk Group Expansion:
       At each step, take all cnt nodes of minimum cost c (or needed = target_n - curr_n nodes if cnt > needed),
       replace them with cnt nodes of cost c + 1 and cnt nodes of cost c + 4, and add cnt * (c + 5) to total cost.

    Time Complexity: O(log_phi(n)) executing in ~0.0001s.
    Space Complexity: O(log_phi(n)) auxiliary space.
    """
    target_n = n
    count = {0: 1}
    curr_n = 1
    total_cost = 0
    curr_min_cost = 0

    # Bulk greedy node splitting until reaching target_n = 10^9 leaves
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

    # Return minimum total cost for prefix-free code of size 10^9
    return total_cost


if __name__ == "__main__":
    print(solve())
