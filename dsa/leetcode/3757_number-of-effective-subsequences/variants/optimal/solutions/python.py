def solve(nums: list[int]) -> int:
    modulus = 1_000_000_007
    aggregate = 0
    for number in nums:
        aggregate |= number

    active_bits = [1 << bit for bit in range(aggregate.bit_length()) if aggregate >> bit & 1]
    masks = 1 << len(active_bits)
    frequency = [0] * masks
    for number in nums:
        signature = 0
        for index, bit in enumerate(active_bits):
            signature |= ((number & bit) != 0) << index
        frequency[signature] += 1

    eligible_count = frequency[:]
    for bit_index in range(len(active_bits)):
        bit = 1 << bit_index
        for mask in range(masks):
            if mask & bit:
                eligible_count[mask] += eligible_count[mask ^ bit]

    power = [1]
    for _ in nums:
        power.append(power[-1] * 2 % modulus)

    universe = masks - 1
    result = 0
    for forbidden in range(1, masks):
        selections = power[eligible_count[universe ^ forbidden]]
        result += selections if forbidden.bit_count() % 2 else -selections
    return result % modulus
