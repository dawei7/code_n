def solve(candies, extraCandies):
    greatest = max(candies)
    return [candy + extraCandies >= greatest for candy in candies]
