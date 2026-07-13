def solve(reward_values: list[int]) -> int:
    # Sort rewards to process them in increasing order
    # This ensures that when we consider reward x, we only care about
    # sums that are strictly less than x.
    rewardValues = sorted(set(reward_values))

    # dp is a bitmask where the i-th bit is 1 if sum i is reachable.
    # Initially, only sum 0 is reachable.
    dp = 1

    for x in rewardValues:
        # We can only add x if the current sum 's' is < x.
        # This corresponds to taking the bits of dp that are less than x,
        # shifting them left by x, and ORing them into the current dp.
        # (dp & ((1 << x) - 1)) extracts bits 0 to x-1.
        dp |= (dp & ((1 << x) - 1)) << x

    # The answer is the highest bit set in the bitmask.
    return dp.bit_length() - 1
