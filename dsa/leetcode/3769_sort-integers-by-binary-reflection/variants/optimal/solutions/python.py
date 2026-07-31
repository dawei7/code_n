def solve(nums: list[int]) -> list[int]:
    def reflected(value: int) -> int:
        result = 0
        while value > 0:
            value, bit = divmod(value, 2)
            result = result * 2 + bit
        return result

    keyed_values = [(reflected(value), value) for value in nums]
    keyed_values.sort()
    return [value for _, value in keyed_values]
