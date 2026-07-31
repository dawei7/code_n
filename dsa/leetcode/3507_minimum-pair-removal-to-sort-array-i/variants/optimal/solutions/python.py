def solve(nums: list[int]) -> int:
    values = nums[:]
    operations = 0

    while any(
        values[index] > values[index + 1]
        for index in range(len(values) - 1)
    ):
        best_index = 0
        best_sum = values[0] + values[1]
        for index in range(1, len(values) - 1):
            pair_sum = values[index] + values[index + 1]
            if pair_sum < best_sum:
                best_sum = pair_sum
                best_index = index

        values[best_index] = best_sum
        values.pop(best_index + 1)
        operations += 1

    return operations
