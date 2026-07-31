def solve(nums, k, m):
    def increment_cost(value, mask):
        missing = mask & ~value
        if missing == 0:
            return 0

        bit = missing.bit_length() - 1
        target = (value >> (bit + 1)) << (bit + 1)
        target |= 1 << bit
        target |= mask & ((1 << bit) - 1)
        return target - value

    answer = 0

    for bit in range(30, -1, -1):
        candidate = answer | (1 << bit)
        costs = [increment_cost(value, candidate) for value in nums]
        costs.sort()
        if sum(costs[:m]) <= k:
            answer = candidate

    return answer
