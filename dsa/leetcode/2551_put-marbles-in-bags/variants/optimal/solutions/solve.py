def solve(weights: list[int], k: int) -> int:
    boundary_costs = sorted(left + right for left, right in zip(weights, weights[1:]))
    cuts = k - 1

    if cuts == 0:
        return 0

    return sum(boundary_costs[-cuts:]) - sum(boundary_costs[:cuts])
