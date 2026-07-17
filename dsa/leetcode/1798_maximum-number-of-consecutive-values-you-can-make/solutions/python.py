def solve(coins: list[int]) -> int:
    reach = 1

    for coin in sorted(coins):
        if coin > reach:
            break
        reach += coin

    return reach
