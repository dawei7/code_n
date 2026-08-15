"""Project Euler Problem 692: Siegbert and Jo.

Find G(23416728348467685), where G(n) = sum_{k=1}^n H(k) and H(k) is the smallest winning move
in Fibonacci Nim on a heap of size k (the smallest component in the Zeckendorf decomposition of k).
"""


def _get_fibonacci(limit: int) -> list[int]:
    f = [0, 1, 1]
    while f[-1] < limit:
        f.append(f[-1] + f[-2])
    return f


def solve(n: int = 23_416_728_348_467_685) -> int:
    """Compute G(n) for n = F_80 using the Zeckendorf Fibonacci Nim sum recurrence S_k = S_{k-1} + S_{k-2} + F_{k-1}."""
    f = _get_fibonacci(n)
    target_k = len(f) - 1

    s = [0] * (target_k + 1)
    s[1] = 0
    s[2] = 1
    s[3] = 3

    for k in range(4, target_k + 1):
        s[k] = s[k - 1] + s[k - 2] + f[k - 1]

    return s[target_k]


if __name__ == "__main__":
    print(solve())
