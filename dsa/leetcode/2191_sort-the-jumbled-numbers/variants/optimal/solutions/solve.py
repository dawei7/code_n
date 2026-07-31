def solve(mapping: list[int], nums: list[int]) -> list[int]:
    def mapped_value(number: int) -> int:
        if number == 0:
            return mapping[0]

        place = 1
        result = 0
        while number:
            number, digit = divmod(number, 10)
            result += mapping[digit] * place
            place *= 10
        return result

    return sorted(nums, key=mapped_value)
