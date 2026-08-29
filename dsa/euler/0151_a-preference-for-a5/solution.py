def solve() -> str:
    """Find the expected number of times the supervisor finds a single sheet in the envelope.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Envelope State Representation & Cutting Rules:
       The envelope starts on Monday with 1 sheet of A1. The supervisor cuts it into:
       1 x A2, 1 x A3, 1 x A4, 1 x A5, and uses 1 x A5 (state at batch 2: (1, 1, 1, 1)).
       Whenever an Ak sheet (k < 5) is picked, it is cut into:
       A(k+1), A(k+2), ..., A5, using one A5 sheet and putting the rest into the envelope.
       State is represented as a 4-tuple (c2, c3, c4, c5) of sheet counts.

    2. State Graph Probability Traversal:
       Starting from root state (1, 1, 1, 1) with probability P = 1.0:
       - Total sheets T = c2 + c3 + c4 + c5.
       - Probability of picking size Ak is ck / T.
       - For batch numbers 2 through 15 (excluding batch 1 and batch 16):
         If total_sheets == 1, add P to expected_singles by linearity of expectation.

    3. Linearity of Expectation:
       E[Singles] = sum_{batch=2}^{15} P(total_sheets == 1 at batch).

    Complexity:
    -----------
    - Time Complexity: O(N_states) where N_states < 500 (~0.001s).
    - Space Complexity: O(N_states) memory for BFS queue.
    """
    # Queue stores tuples: (state, probability, batch_number)
    # State: (c2, c3, c4, c5)
    queue = [((1, 1, 1, 1), 1.0, 2)]
    expected_singles = 0.0

    while queue:
        state, prob, batch_num = queue.pop(0)
        c2, c3, c4, c5 = state
        total_sheets = c2 + c3 + c4 + c5
        if total_sheets == 0:
            continue

        # Check if single sheet found during intermediate batches (2 to 15)
        if batch_num not in (1, 16) and total_sheets == 1:
            expected_singles += prob

        # Transition 1: Pick A2 -> generates (A3, A4, A5), uses A5
        if c2 > 0:
            p = c2 / total_sheets
            queue.append(
                ((c2 - 1, c3 + 1, c4 + 1, c5 + 1), prob * p, batch_num + 1)
            )

        # Transition 2: Pick A3 -> generates (A4, A5), uses A5
        if c3 > 0:
            p = c3 / total_sheets
            queue.append(
                ((c2, c3 - 1, c4 + 1, c5 + 1), prob * p, batch_num + 1)
            )

        # Transition 3: Pick A4 -> generates A5, uses A5
        if c4 > 0:
            p = c4 / total_sheets
            queue.append(
                ((c2, c3, c4 - 1, c5 + 1), prob * p, batch_num + 1)
            )

        # Transition 4: Pick A5 -> uses A5 directly
        if c5 > 0:
            p = c5 / total_sheets
            queue.append(((c2, c3, c4, c5 - 1), prob * p, batch_num + 1))

    # Format result to 6 decimal places as required by problem specification
    return f"{expected_singles:.6f}"


if __name__ == "__main__":
    print(solve())
