def solve(nums: list[int]) -> int:
    total = 0
    n = len(nums)

    for left in range(n):
        seen = {nums[left]}
        imbalance = 0

        for right in range(left + 1, n):
            value = nums[right]

            if value not in seen:
                has_lower_neighbor = value - 1 in seen
                has_upper_neighbor = value + 1 in seen

                if has_lower_neighbor and has_upper_neighbor:
                    imbalance -= 1
                elif not has_lower_neighbor and not has_upper_neighbor:
                    imbalance += 1

                seen.add(value)

            total += imbalance

    return total
