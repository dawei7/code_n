def solve(
    n: int,
    present: list[int],
    future: list[int],
    hierarchy: list[list[int]],
    budget: int,
) -> int:
    children: list[list[int]] = [[] for _ in range(n)]
    for boss, employee in hierarchy:
        children[boss - 1].append(employee - 1)

    unreachable = -10**9

    def merge(left: list[int], right: list[int]) -> list[int]:
        combined = [unreachable] * (budget + 1)
        for left_cost, left_profit in enumerate(left):
            if left_profit == unreachable:
                continue
            for right_cost in range(budget - left_cost + 1):
                right_profit = right[right_cost]
                if right_profit != unreachable:
                    total_cost = left_cost + right_cost
                    combined[total_cost] = max(
                        combined[total_cost], left_profit + right_profit
                    )
        return combined

    def visit(employee: int) -> tuple[list[int], list[int]]:
        skip_children = [0] + [unreachable] * budget
        buy_children = skip_children.copy()

        for child in children[employee]:
            child_without_discount, child_with_discount = visit(child)
            skip_children = merge(skip_children, child_without_discount)
            buy_children = merge(buy_children, child_with_discount)

        results: list[list[int]] = []
        for price in (present[employee], present[employee] // 2):
            current = skip_children.copy()
            for child_cost in range(budget - price + 1):
                child_profit = buy_children[child_cost]
                if child_profit != unreachable:
                    total_cost = child_cost + price
                    current[total_cost] = max(
                        current[total_cost],
                        child_profit + future[employee] - price,
                    )
            results.append(current)

        return results[0], results[1]

    root_without_discount, _ = visit(0)
    return max(root_without_discount)
