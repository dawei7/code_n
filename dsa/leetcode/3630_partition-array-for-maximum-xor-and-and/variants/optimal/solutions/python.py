def solve(nums: list[int]) -> int:
    n = len(nums)
    subset_count = 1 << n
    full_mask = subset_count - 1
    subset_xor = [0] * subset_count
    subset_and = [0] * subset_count

    for mask in range(1, subset_count):
        bit = mask & -mask
        index = bit.bit_length() - 1
        previous = mask ^ bit
        subset_xor[mask] = subset_xor[previous] ^ nums[index]
        subset_and[mask] = (
            nums[index]
            if previous == 0
            else subset_and[previous] & nums[index]
        )

    answer = 0
    value_mask = (1 << 30) - 1
    for outside_b in range(subset_count):
        total_xor = subset_xor[outside_b]
        keep_bits = value_mask ^ total_xor
        basis = [0] * 30
        remaining = outside_b

        while remaining:
            bit = remaining & -remaining
            value = nums[bit.bit_length() - 1] & keep_bits
            while value:
                pivot = value.bit_length() - 1
                if basis[pivot]:
                    value ^= basis[pivot]
                else:
                    basis[pivot] = value
                    break
            remaining ^= bit

        best_projected_xor = 0
        for pivot in range(29, -1, -1):
            best_projected_xor = max(
                best_projected_xor,
                best_projected_xor ^ basis[pivot],
            )

        b_mask = full_mask ^ outside_b
        answer = max(
            answer,
            subset_and[b_mask] + total_xor + 2 * best_projected_xor,
        )

    return answer

