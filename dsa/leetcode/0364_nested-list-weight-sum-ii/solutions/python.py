"""Optimal app-local solution for LeetCode 364: Nested List Weight Sum II."""


def solve(nested_list: list) -> int:
    depth_sums: list[int] = []
    maximum_integer_depth = 0

    def collect(values: list, depth: int) -> None:
        nonlocal maximum_integer_depth
        for value in values:
            if isinstance(value, int):
                while len(depth_sums) < depth:
                    depth_sums.append(0)
                depth_sums[depth - 1] += value
                maximum_integer_depth = max(maximum_integer_depth, depth)
            else:
                collect(value, depth + 1)

    collect(nested_list, 1)
    return sum(
        depth_sum * (maximum_integer_depth - depth + 1)
        for depth, depth_sum in enumerate(depth_sums, start=1)
    )

