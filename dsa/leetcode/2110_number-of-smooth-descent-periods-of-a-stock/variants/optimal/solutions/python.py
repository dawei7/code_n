def solve(prices: list[int]) -> int:
    ending_here = 1
    total = 1

    for index in range(1, len(prices)):
        if prices[index - 1] - prices[index] == 1:
            ending_here += 1
        else:
            ending_here = 1
        total += ending_here

    return total
