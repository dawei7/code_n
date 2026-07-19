def solve(nums: list[int]) -> int:
    values = list(nums)
    operations = 0

    def is_sorted() -> bool:
        return all(values[i] <= values[i + 1] for i in range(len(values) - 1))

    while not is_sorted():
        best_index = 0
        best_sum = values[0] + values[1]
        for index in range(1, len(values) - 1):
            pair_sum = values[index] + values[index + 1]
            if pair_sum < best_sum:
                best_sum = pair_sum
                best_index = index
        values[best_index : best_index + 2] = [best_sum]
        operations += 1

    return operations
