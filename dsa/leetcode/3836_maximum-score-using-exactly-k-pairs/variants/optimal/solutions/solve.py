def solve(nums1: list[int], nums2: list[int], k: int) -> int:
    left_values = nums1
    right_values = nums2
    if len(right_values) > len(left_values):
        left_values, right_values = right_values, left_values

    width = len(right_values)
    negative_infinity = -(10**30)
    previous = [[0] * (width + 1)] + [[negative_infinity] * (width + 1) for _ in range(k)]

    for left_value in left_values:
        current = [[0] * (width + 1)] + [[negative_infinity] * (width + 1) for _ in range(k)]

        for pair_count in range(1, k + 1):
            for right_index, right_value in enumerate(right_values, start=1):
                best = max(
                    previous[pair_count][right_index],
                    current[pair_count][right_index - 1],
                )
                diagonal = previous[pair_count - 1][right_index - 1]
                if diagonal != negative_infinity:
                    best = max(best, diagonal + left_value * right_value)
                current[pair_count][right_index] = best

        previous = current

    return previous[k][width]
