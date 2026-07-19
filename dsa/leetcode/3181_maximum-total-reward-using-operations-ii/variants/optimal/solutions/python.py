def solve(reward_values: list[int]) -> int:
    # Sort and remove duplicates to optimize the DP transitions
    rewards = sorted(set(reward_values))

    # bits represents the set of reachable total rewards.
    # If the i-th bit is 1, then a total reward of i is possible.
    bits = 1

    for x in rewards:
        # We can only pick reward x if current_total < x.
        # This means we only care about reachable totals < x.
        # The mask (1 << x) - 1 extracts all bits from 0 to x-1.
        # Shifting by x adds x to all those reachable totals.
        bits |= (bits & ((1 << x) - 1)) << x

    # The answer is the highest bit set in the bitmask.
    return bits.bit_length() - 1
