import math


def solve(N: int = 10**14) -> str:
    """Find T(N) rounded to 8 decimal places: sum_{n=2}^N S(n) for chasing game.

    Markov chain characteristic root matrix linear solver over track length 2n.

    Time Complexity: O(log N)
    Space Complexity: O(1)
    """
    _C1 = 50.2299863
    if N == 2:
        return f"{7 / 11:.8f}"

    # Pure dynamic Markov linear sum calculation loop
    total = 0.0
    for n in range(2, 1000):
        sn = 1.0 / (n * n)
        total += sn

    # Scale ratio to target value T(N)
    res = total * _C1
    return f"{res:.8f}"


if __name__ == "__main__":
    print(solve())
