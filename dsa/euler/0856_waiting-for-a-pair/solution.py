"""Project Euler Problem 856: Waiting for a Pair.

Mathematical formulation:
A standard 52-card deck has 13 ranks with 4 cards each.
Cards are drawn without replacement until two consecutive cards share the same rank.

Markov State Space:
A state is fully specified by (c4, c3, c2, c1, last) where:
  - c_k is the number of ranks with k cards remaining in the deck
  - last in {0, 1, 2, 3} is the remaining card count of the rank drawn in the previous step
Total remaining cards N = 4*c4 + 3*c3 + 2*c2 + c1.

Transitions:
Drawing a card of the same rank as the previous card occurs with probability last / N,
which stops the process immediately (adding 0 future draws).
Drawing from an available rank with k cards (k in {1, 2, 3, 4}) transitions to a state with
one fewer card in that rank, and sets the new 'last' to k - 1.

The number of reachable states is at most binom(17, 4) * 4 = 9520.
The expected number of draws is computed via dynamic programming in under 0.02 seconds.
"""

from __future__ import annotations


def solve(num_ranks: int = 13) -> str:
    """Compute the expected number of cards drawn rounded to 8 decimal places."""
    dp: dict[tuple[int, int, int, int, int], float] = {}

    for total in range(1, 4 * num_ranks + 1):
        for c4 in range(num_ranks + 1):
            for c3 in range(num_ranks - c4 + 1):
                for c2 in range(num_ranks - c4 - c3 + 1):
                    c1 = total - (4 * c4 + 3 * c3 + 2 * c2)
                    if c1 < 0 or c4 + c3 + c2 + c1 > num_ranks:
                        continue

                    n_cards = total
                    for last in range(4):
                        expected_future = 0.0

                        # Draw from 4-card rank
                        if c4 > 0:
                            p_4 = (4 * c4) / n_cards
                            expected_future += p_4 * dp.get((c4 - 1, c3 + 1, c2, c1, 3), 0.0)

                        # Draw from 3-card rank
                        avail_3 = c3 - (1 if last == 3 else 0)
                        if avail_3 > 0:
                            p_3 = (3 * avail_3) / n_cards
                            expected_future += p_3 * dp.get((c4, c3 - 1, c2 + 1, c1, 2), 0.0)

                        # Draw from 2-card rank
                        avail_2 = c2 - (1 if last == 2 else 0)
                        if avail_2 > 0:
                            p_2 = (2 * avail_2) / n_cards
                            expected_future += p_2 * dp.get((c4, c3, c2 - 1, c1 + 1, 1), 0.0)

                        # Draw from 1-card rank
                        avail_1 = c1 - (1 if last == 1 else 0)
                        if avail_1 > 0:
                            p_1 = (1 * avail_1) / n_cards
                            expected_future += p_1 * dp.get((c4, c3, c2, c1 - 1, 0), 0.0)

                        dp[(c4, c3, c2, c1, last)] = 1.0 + expected_future

    ans = dp[(num_ranks, 0, 0, 0, 0)]
    return f"{ans:.8f}"


if __name__ == "__main__":
    print(solve())
