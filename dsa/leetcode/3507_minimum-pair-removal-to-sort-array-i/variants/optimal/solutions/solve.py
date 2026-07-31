def solve(nums: list[int]) -> int:
    values = nums[:]
    operations = 0

    while any(values[index] > values[index + 1] for index in range(len(values) - 1)):
        best_index = 0
        for index in range(1, len(values) - 1):
            if values[index] + values[index + 1] < values[best_index] + values[best_index + 1]:
                best_index = index

        values[best_index] += values[best_index + 1]
        values.pop(best_index + 1)
        operations += 1

    return operations
