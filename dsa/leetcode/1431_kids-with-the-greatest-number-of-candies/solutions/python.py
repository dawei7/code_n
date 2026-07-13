def solve(candies, extra_candies):
    best = max(candies) if candies else 0
    return [candy + extra_candies >= best for candy in candies]
