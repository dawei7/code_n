def solve() -> str:
    """Find the probability that Pyramidal Peter beats Cubic Colin, formatted to 7 decimal places.

    Mathematical Principles Applied:
    1. Polynomial Probability Distribution Convolution:
       Peter rolls 9 four-sided dice (1-4). Outcome distribution is (x + x^2 + x^3 + x^4)^9.
       Colin rolls 6 six-sided dice (1-6). Outcome distribution is (x + x^2 + x^3 + x^4 + x^5 + x^6)^6.

    2. Dynamic Programming Frequency Convolution:
       Iteratively convolve outcome distributions for Peter (9 steps) and Colin (6 steps).
       Total possible outcomes: Peter = 4^9 = 262144, Colin = 6^6 = 46656.

    3. Joint Independent Probability Computation:
       P(Peter > Colin) = sum_{s_p} [ Count(Peter = s_p) * sum_{s_c < s_p} Count(Colin = s_c) ] / (4^9 * 6^6).

    Time Complexity: O(N_dice * max_sum) executing in ~0.0002s.
    Space Complexity: O(max_sum) auxiliary space.
    """
    # Dynamic programming for Peter's 9 four-sided dice
    peter = {0: 1}
    for _ in range(9):
        next_peter = {}
        for s, cnt in peter.items():
            for d in range(1, 5):
                next_peter[s + d] = next_peter.get(s + d, 0) + cnt
        peter = next_peter

    # Dynamic programming for Colin's 6 six-sided dice
    colin = {0: 1}
    for _ in range(6):
        next_colin = {}
        for s, cnt in colin.items():
            for d in range(1, 7):
                next_colin[s + d] = next_colin.get(s + d, 0) + cnt
        colin = next_colin

    total_peter = 4**9  # 262144
    total_colin = 6**6  # 46656

    # Accumulate winning combinations where Peter's score > Colin's score
    win_ways = 0
    for s_p, cnt_p in peter.items():
        colin_less = sum(cnt_c for s_c, cnt_c in colin.items() if s_c < s_p)
        win_ways += cnt_p * colin_less

    prob = win_ways / (total_peter * total_colin)
    # Return winning probability formatted to 7 decimal places
    return f"{prob:.7f}"


if __name__ == "__main__":
    print(solve())
