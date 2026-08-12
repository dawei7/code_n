from fractions import Fraction


def solve(
    n_squares: int = 500, croaks: str = "PPPPNNPPPNPPNPN"
) -> str:
    """Find the exact rational probability p/q that Susan hears the 15 croaks sequence PPPPNNPPPNPPNPN.
    
    Time Complexity: O(n_squares * len(croaks)) via Exact Fraction Dynamic Programming
    Space Complexity: O(n_squares)
    """
    is_p = [True] * (n_squares + 1)
    is_p[0] = is_p[1] = False
    for i in range(2, int(n_squares**0.5) + 1):
        if is_p[i]:
            for j in range(i * i, n_squares + 1, i):
                is_p[j] = False

    def emit_prob(x, c):
        p_true = is_p[x]
        if c == "P":
            return Fraction(2, 3) if p_true else Fraction(1, 3)
        else:
            return Fraction(1, 3) if p_true else Fraction(2, 3)

    state = [Fraction(0)] * (n_squares + 1)
    for x in range(1, n_squares + 1):
        state[x] = Fraction(1, n_squares) * emit_prob(x, croaks[0])

    for t in range(1, len(croaks)):
        next_state = [Fraction(0)] * (n_squares + 1)
        for x in range(1, n_squares + 1):
            if state[x] == 0:
                continue
            if x == 1:
                next_state[2] += state[x]
            elif x == n_squares:
                next_state[n_squares - 1] += state[x]
            else:
                next_state[x - 1] += state[x] * Fraction(1, 2)
                next_state[x + 1] += state[x] * Fraction(1, 2)

        for x in range(1, n_squares + 1):
            next_state[x] *= emit_prob(x, croaks[t])

        state = next_state

    return str(sum(state))
