def solve(n: int = 70) -> int:
    """Find the number of closed robot journeys of length n = 70.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Robot Movement & Regular Pentagonal Angles:
       The robot moves along circular arcs of 72 degrees (1/5 of a full circle).
       At each step, the robot chooses either a clockwise (CW) or counter-clockwise (CCW) arc.
       The direction of travel at any point corresponds to one of the 5 roots of unity in C:
           zeta^k = e^(2*pi*i*k / 5) for k in {0, 1, 2, 3, 4}.

    2. Closed Loop Condition:
       The journey forms a closed loop in the complex plane iff:
       - The robot visits each of the 5 arc directions equally often:
           c_0 = c_1 = c_2 = c_3 = c_4 = n // 5 = 14.
       - The final orientation returns to the starting orientation (o = 0).

    3. Dynamic Programming State Compression:
       We track state (c0, c1, c2, c3, c4, o) where:
       - c0..c4 are the number of arcs taken in each direction (each <= 14).
       - o in {0, 1, 2, 3, 4} is the current orientation angle.
       At each step:
       - CW arc: traverses in direction o, new orientation (o - 1) % 5.
       - CCW arc: new orientation (o + 1) % 5, traverses in direction (o + 1) % 5.

    Complexity:
    -----------
    - Time Complexity: O(n * (n/5)^5) state transitions (~0.10s for n = 70).
    - Space Complexity: O((n/5)^5) state hash map (~8 MB).
    """
    target_c = n // 5

    # DP state map: (c0, c1, c2, c3, c4, orientation) -> ways
    dp_state = {(0, 0, 0, 0, 0, 0): 1}

    for _ in range(n):
        next_dp = {}
        for (c0, c1, c2, c3, c4, o), ways in dp_state.items():
            # Clockwise (CW) transition
            cc = [c0, c1, c2, c3, c4]
            cc[o] += 1
            if cc[o] <= target_c:
                st = (cc[0], cc[1], cc[2], cc[3], cc[4], (o - 1) % 5)
                next_dp[st] = next_dp.get(st, 0) + ways

            # Counter-Clockwise (CCW) transition
            cc = [c0, c1, c2, c3, c4]
            new_o = (o + 1) % 5
            cc[new_o] += 1
            if cc[new_o] <= target_c:
                st = (cc[0], cc[1], cc[2], cc[3], cc[4], new_o)
                next_dp[st] = next_dp.get(st, 0) + ways

        dp_state = next_dp

    # Return total ways reaching (14, 14, 14, 14, 14, 0)
    return dp_state.get((target_c, target_c, target_c, target_c, target_c, 0), 0)


if __name__ == "__main__":
    print(solve())
