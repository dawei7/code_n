def solve(nums1: list[int], nums2: list[int]) -> int:
    def next_value(previous: int, parity: int) -> int:
        candidate = previous + 1
        if candidate % 2 != parity:
            candidate += 1
        return candidate

    second_length = len(nums2)
    previous_row = [0] * (second_length + 1)
    for second_index, parity in enumerate(nums2, 1):
        previous_row[second_index] = next_value(
            previous_row[second_index - 1], parity
        )

    for first_parity in nums1:
        current_row = [0] * (second_length + 1)
        current_row[0] = next_value(previous_row[0], first_parity)

        for second_index, second_parity in enumerate(nums2, 1):
            take_first = next_value(previous_row[second_index], first_parity)
            take_second = next_value(
                current_row[second_index - 1], second_parity
            )
            current_row[second_index] = min(take_first, take_second)

        previous_row = current_row

    return previous_row[second_length]
