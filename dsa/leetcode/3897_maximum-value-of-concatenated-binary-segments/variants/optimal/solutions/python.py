def solve(nums1: list[int], nums0: list[int]) -> int:
    segments = list(zip(nums1, nums0))

    def order(segment: tuple[int, int]) -> tuple[int, int, int]:
        ones, zeros = segment
        if zeros == 0:
            return (0, 0, 0)
        if ones == 0:
            return (2, 0, 0)
        return (1, -ones, zeros)

    segments.sort(key=order)

    modulo = 1_000_000_007
    value = 0
    for ones, zeros in segments:
        ones_power = pow(2, ones, modulo)
        value = (value * ones_power + ones_power - 1) % modulo
        value = value * pow(2, zeros, modulo) % modulo
    return value
