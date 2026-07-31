def solve(nums: list[int], k: int, queries: list[list[int]]) -> list[int]:
    values = [number // k for number in nums]
    coordinates = sorted(set(values))
    ranks = {value: index for index, value in enumerate(coordinates)}
    width = max(1, (len(coordinates) - 1).bit_length())

    ordered = [(ranks[value], value) for value in values]
    zero_prefixes = []
    zero_sum_prefixes = []
    zero_totals = []
    for shift in range(width - 1, -1, -1):
        count_prefix = [0]
        sum_prefix = [0]
        zero_items = []
        one_items = []
        for item in ordered:
            is_zero = (item[0] >> shift) & 1 == 0
            count_prefix.append(count_prefix[-1] + is_zero)
            sum_prefix.append(sum_prefix[-1] + (item[1] if is_zero else 0))
            (zero_items if is_zero else one_items).append(item)
        zero_prefixes.append(count_prefix)
        zero_sum_prefixes.append(sum_prefix)
        zero_totals.append(len(zero_items))
        ordered = zero_items + one_items

    value_prefix = [0]
    for value in values:
        value_prefix.append(value_prefix[-1] + value)

    changes = [0] * len(nums)
    for index in range(1, len(nums)):
        changes[index] = changes[index - 1] + (
            nums[index] % k != nums[index - 1] % k
        )

    answers = []
    for source_left, source_right in queries:
        if changes[source_left] != changes[source_right]:
            answers.append(-1)
            continue

        left = source_left
        right = source_right + 1
        length = right - left
        order = (length + 1) // 2
        median_rank = 0
        below_count = 0
        below_sum = 0
        for level, shift in enumerate(range(width - 1, -1, -1)):
            count_prefix = zero_prefixes[level]
            sum_prefix = zero_sum_prefixes[level]
            zero_left = count_prefix[left]
            zero_right = count_prefix[right]
            zero_count = zero_right - zero_left
            if order <= zero_count:
                left = zero_left
                right = zero_right
            else:
                below_count += zero_count
                below_sum += sum_prefix[right] - sum_prefix[left]
                order -= zero_count
                median_rank |= 1 << shift
                zero_total = zero_totals[level]
                left = zero_total + left - zero_left
                right = zero_total + right - zero_right

        median = coordinates[median_rank]
        equal_count = right - left
        left_count = below_count + equal_count
        left_sum = below_sum + median * equal_count
        total_sum = value_prefix[source_right + 1] - value_prefix[source_left]
        right_count = length - left_count
        right_sum = total_sum - left_sum
        answers.append(
            median * left_count - left_sum + right_sum - median * right_count
        )
    return answers
