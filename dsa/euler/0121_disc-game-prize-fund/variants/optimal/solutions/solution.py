from fractions import Fraction


def solve(turns: int = 15) -> int:
    """Find maximum prize fund allocated for a 15-turn disc game.
    
    Time Complexity: O(N^2)
    Space Complexity: O(N)
    """
    # dp[b] stores exact fraction probability of getting b blue discs
    dp = [Fraction(0)] * (turns + 1)
    dp[0] = Fraction(1)

    for k in range(1, turns + 1):
        next_dp = [Fraction(0)] * (turns + 1)
        prob_blue = Fraction(1, k + 1)
        prob_red = Fraction(k, k + 1)

        for b in range(k + 1):
            # Case 1: Draw red
            next_dp[b] += dp[b] * prob_red
            # Case 2: Draw blue
            if b > 0:
                next_dp[b] += dp[b - 1] * prob_blue

        dp = next_dp

    min_blue_to_win = (turns // 2) + 1
    p_win = sum(dp[min_blue_to_win:])

    return int(1 / p_win)
