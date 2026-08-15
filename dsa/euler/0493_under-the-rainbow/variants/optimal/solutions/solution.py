"""Project Euler Problem 493: Under the Rainbow.

Find the expected number of distinct colours in 20 randomly picked balls from an urn
containing 70 balls (10 for each of the 7 rainbow colours), rounded to 9 decimal places.
"""


def solve(
    total_balls: int = 70,
    colors: int = 7,
    balls_per_color: int = 10,
    draw_count: int = 20,
) -> str:
    """Compute expected distinct colors using Linearity of Expectation and sequential drawing loop."""
    expected_distinct = 0.0
    for _ in range(colors):
        prob_absent = 1.0
        rem_non_color = total_balls - balls_per_color
        rem_total = total_balls
        for d in range(draw_count):
            prob_absent *= (rem_non_color - d) / (rem_total - d)
        expected_distinct += 1.0 - prob_absent

    return f"{expected_distinct:.9f}"


if __name__ == "__main__":
    print(solve())
