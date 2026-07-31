def solve(nums: list[int]) -> list[int]:
    def distance(value: int) -> int:
        bits = bin(value)[2:]
        length = len(bits)
        half_length = (length + 1) // 2
        prefix = int(bits[:half_length], 2)

        candidates = {
            (1 << (length - 1)) - 1,
            (1 << length) + 1,
        }
        for half in (prefix - 1, prefix, prefix + 1):
            if half <= 0:
                continue
            left = bin(half)[2:]
            reflected = left[:-1] if length % 2 else left
            candidates.add(int(left + reflected[::-1], 2))

        return min(abs(value - candidate) for candidate in candidates)

    return [distance(value) for value in nums]
