def solve(nums: list[int], k: int, m: int) -> int:
    counts: dict[int, int] = {}
    left = 0
    distinct = 0
    qualified = 0
    removable_prefix = 0
    answer = 0

    for value in nums:
        previous = counts.get(value, 0)
        counts[value] = previous + 1

        if previous == 0:
            distinct += 1
        if previous + 1 == m:
            qualified += 1

        if distinct > k:
            while distinct > k:
                outgoing = nums[left]
                if counts[outgoing] == m:
                    qualified -= 1

                counts[outgoing] -= 1
                left += 1

                if counts[outgoing] == 0:
                    del counts[outgoing]
                    distinct -= 1

            removable_prefix = 0

        if distinct == k and qualified == k:
            while counts[nums[left]] > m:
                counts[nums[left]] -= 1
                left += 1
                removable_prefix += 1

            answer += removable_prefix + 1

    return answer
