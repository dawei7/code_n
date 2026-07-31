def solve(power: list[int]) -> int:
    monster_count = len(power)
    full_mask = (1 << monster_count) - 1
    minimum_days = [10**30] * (full_mask + 1)
    minimum_days[0] = 0

    for mask in range(full_mask + 1):
        gain = mask.bit_count() + 1
        for monster, required_power in enumerate(power):
            monster_bit = 1 << monster
            if mask & monster_bit:
                continue
            next_mask = mask | monster_bit
            days = (required_power + gain - 1) // gain
            minimum_days[next_mask] = min(
                minimum_days[next_mask],
                minimum_days[mask] + days,
            )

    return minimum_days[full_mask]
