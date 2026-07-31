def solve(nums: list[int]) -> int:
    n = len(nums)
    empty_position = nums.index(0)

    def operations(zero_at_start: bool) -> int:
        seen = [False] * n
        moves = 0

        for start in range(n):
            if seen[start]:
                continue

            position = start
            length = 0
            contains_empty = False
            while not seen[position]:
                seen[position] = True
                length += 1
                contains_empty = contains_empty or position == empty_position
                value = nums[position]
                if zero_at_start:
                    position = value
                else:
                    position = n - 1 if value == 0 else value - 1

            if length > 1:
                moves += length - 1 if contains_empty else length + 1

        return moves

    return min(operations(True), operations(False))
