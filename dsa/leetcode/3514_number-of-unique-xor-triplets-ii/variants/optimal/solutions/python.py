def solve(nums: list[int]) -> int:
    width = 1 << max(nums).bit_length()
    present = set(nums)
    spectrum = [int(value in present) for value in range(width)]

    def transform(values: list[int]) -> None:
        block = 1
        while block < len(values):
            for start in range(0, len(values), 2 * block):
                for index in range(start, start + block):
                    left, right = values[index], values[index + block]
                    values[index], values[index + block] = left + right, left - right
            block *= 2

    transform(spectrum)
    spectrum = [value * value * value for value in spectrum]
    transform(spectrum)
    return sum(value != 0 for value in spectrum)
