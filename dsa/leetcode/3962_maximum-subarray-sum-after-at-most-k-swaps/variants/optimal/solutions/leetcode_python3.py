from bisect import bisect_left


class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        n = len(nums)
        values = sorted(set(nums))
        value_count = len(values)
        ranks = {value: index for index, value in enumerate(values)}

        global_frequency = [0] * value_count
        for value in nums:
            global_frequency[ranks[value]] += 1

        global_prefix = []
        running_count = 0
        for frequency in global_frequency:
            running_count += frequency
            global_prefix.append(running_count)

        pivot = [0] * (n + 1)
        prefix_at_pivot = [0] * (n + 1)
        for outside_size in range(1, n):
            index = bisect_left(global_prefix, outside_size)
            pivot[outside_size] = index
            prefix_at_pivot[outside_size] = global_prefix[index]

        total_count_tree = [0] * (value_count + 1)
        total_sum_tree = [0] * (value_count + 1)
        for value in nums:
            index = ranks[value] + 1
            while index <= value_count:
                total_count_tree[index] += 1
                total_sum_tree[index] += value
                index += index & -index

        total_sum = sum(nums)
        bit_step = 1 << (value_count.bit_length() - 1)
        answer = -(10**30)

        for left in range(n):
            inside_count_tree = [0] * (value_count + 1)
            inside_sum_tree = [0] * (value_count + 1)
            inside_frequency = [0] * value_count
            current_sum = 0

            for right in range(left, n):
                value = nums[right]
                position = ranks[value]
                inside_frequency[position] += 1
                current_sum += value

                index = position + 1
                while index <= value_count:
                    inside_count_tree[index] += 1
                    inside_sum_tree[index] += value
                    index += index & -index

                inside_size = right - left + 1
                outside_size = n - inside_size
                swaps = 0

                if k and outside_size:
                    position = pivot[outside_size]
                    index = position
                    inside_before = 0
                    while index:
                        inside_before += inside_count_tree[index]
                        index -= index & -index

                    inside_through = inside_before + inside_frequency[position]
                    profitable = max(
                        inside_before,
                        outside_size
                        - prefix_at_pivot[outside_size]
                        + inside_through,
                    )
                    swaps = min(k, profitable)

                candidate = current_sum
                if swaps:
                    index = 0
                    selected_count = 0
                    selected_sum = 0
                    step = bit_step
                    while step:
                        next_index = index + step
                        if (
                            next_index <= value_count
                            and selected_count + inside_count_tree[next_index]
                            < swaps
                        ):
                            selected_count += inside_count_tree[next_index]
                            selected_sum += inside_sum_tree[next_index]
                            index = next_index
                        step >>= 1
                    inside_smallest_sum = selected_sum + (
                        swaps - selected_count
                    ) * values[index]

                    outside_small_count = outside_size - swaps
                    if outside_small_count:
                        index = 0
                        selected_count = 0
                        selected_sum = 0
                        step = bit_step
                        while step:
                            next_index = index + step
                            if next_index <= value_count:
                                block_count = (
                                    total_count_tree[next_index]
                                    - inside_count_tree[next_index]
                                )
                                if selected_count + block_count < outside_small_count:
                                    selected_count += block_count
                                    selected_sum += (
                                        total_sum_tree[next_index]
                                        - inside_sum_tree[next_index]
                                    )
                                    index = next_index
                            step >>= 1
                        outside_smallest_sum = selected_sum + (
                            outside_small_count - selected_count
                        ) * values[index]
                    else:
                        outside_smallest_sum = 0

                    outside_largest_sum = (
                        total_sum - current_sum - outside_smallest_sum
                    )
                    candidate += outside_largest_sum - inside_smallest_sum

                answer = max(answer, candidate)

        return answer
