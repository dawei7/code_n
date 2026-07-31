def solve(nums: list[int]) -> int:
    n = len(nums)
    prefix_matches = [0] * n
    left = 0
    right = 0
    for position in range(1, n):
        if position <= right:
            prefix_matches[position] = min(
                right - position + 1,
                prefix_matches[position - left],
            )
        while (
            position + prefix_matches[position] < n
            and nums[prefix_matches[position]]
            == nums[position + prefix_matches[position]]
        ):
            prefix_matches[position] += 1
        if position + prefix_matches[position] - 1 > right:
            left = position
            right = position + prefix_matches[position] - 1

    answer = 0
    next_lcp = [0] * (n + 1)
    for first_cut in range(n - 2, 0, -1):
        current_lcp = [0] * (n + 1)
        first_can_prefix_second = (
            prefix_matches[first_cut] >= first_cut
        )
        for second_cut in range(n - 1, first_cut, -1):
            if nums[first_cut] == nums[second_cut]:
                current_lcp[second_cut] = (
                    1 + next_lcp[second_cut + 1]
                )

            second_length = second_cut - first_cut
            if (
                first_can_prefix_second
                and first_cut <= second_length
            ) or (
                second_length <= n - second_cut
                and current_lcp[second_cut] >= second_length
            ):
                answer += 1
        next_lcp = current_lcp

    return answer
