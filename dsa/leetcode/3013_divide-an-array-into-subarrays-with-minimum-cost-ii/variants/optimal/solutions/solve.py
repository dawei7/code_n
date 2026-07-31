def solve(nums: list[int], k: int, dist: int) -> int:
    values = sorted(set(nums[1:]))
    ranks = {value: index + 1 for index, value in enumerate(values)}
    size = len(values)
    counts = [0] * (size + 1)
    sums = [0] * (size + 1)

    def update(tree: list[int], index: int, delta: int) -> None:
        while index <= size:
            tree[index] += delta
            index += index & -index

    def smallest_sum(amount: int) -> int:
        index = 0
        prefix_count = 0
        prefix_sum = 0
        step = 1 << (size.bit_length() - 1)
        while step:
            next_index = index + step
            if next_index <= size and prefix_count + counts[next_index] < amount:
                index = next_index
                prefix_count += counts[next_index]
                prefix_sum += sums[next_index]
            step >>= 1
        return prefix_sum + (amount - prefix_count) * values[index]

    answer = float("inf")
    needed = k - 2

    for right in range(1, len(nums)):
        added = right - 1
        if added >= 1:
            rank = ranks[nums[added]]
            update(counts, rank, 1)
            update(sums, rank, nums[added])

        removed = right - dist - 1
        if removed >= 1:
            rank = ranks[nums[removed]]
            update(counts, rank, -1)
            update(sums, rank, -nums[removed])

        window_size = right - max(1, right - dist)
        if window_size >= needed:
            answer = min(answer, nums[right] + smallest_sum(needed))

    return nums[0] + answer
