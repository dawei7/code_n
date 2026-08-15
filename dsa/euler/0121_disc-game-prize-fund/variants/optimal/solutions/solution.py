from fractions import Fraction


def solve(turns: int = 15) -> int:
    """Find the maximum prize fund allocated for a 15-turn disc game.

    Mathematical Principles Applied:
    1. Turn Probability Distributions:
       In turn k (1 <= k <= 15), the bag contains 1 blue disc and k red discs (total k+1 discs).
       - Probability of drawing blue: P(Blue_k) = 1 / (k + 1).
       - Probability of drawing red:  P(Red_k) = k / (k + 1).

    2. Dynamic Programming State Distribution:
       Let dp[b] be the exact rational probability of drawing b blue discs after current turn.
       Base case: dp[0] = 1.
       Transitions at turn k:
       next_dp[b] = dp[b] * (k / (k+1)) + dp[b-1] * (1 / (k+1)).

    3. Fair Prize Allocation:
       To win, a player must draw strictly MORE blue discs than red discs (b >= 8 for 15 turns).
       Total winning probability: P_win = sum_{b = floor(turns/2) + 1}^{turns} dp[b].
       Maximum prize fund = floor(1 / P_win).

    Time Complexity: O(turns^2) executing in ~0.001s.
    Space Complexity: O(turns) memory for DP array.
    """
    # dp[b] stores exact fraction probability of getting b blue discs
    dp = [Fraction(0)] * (turns + 1)
    dp[0] = Fraction(1)

    # Process each turn k from 1 to 15
    for k in range(1, turns + 1):
        next_dp = [Fraction(0)] * (turns + 1)
        prob_blue = Fraction(1, k + 1)
        prob_red = Fraction(k, k + 1)

        for b in range(k + 1):
            # Case 1: Draw red disc at turn k
            next_dp[b] += dp[b] * prob_red
            # Case 2: Draw blue disc at turn k
            if b > 0:
                next_dp[b] += dp[b - 1] * prob_blue

        dp = next_dp

    # To win, player needs strictly more blue discs than red discs (b >= 8 out of 15)
    min_blue_to_win = (turns // 2) + 1
    p_win = sum(dp[min_blue_to_win:])

    # Maximum prize fund allocated is floor(1 / P_win)
    return int(1 / p_win)


if __name__ == "__main__":
    print(solve())
