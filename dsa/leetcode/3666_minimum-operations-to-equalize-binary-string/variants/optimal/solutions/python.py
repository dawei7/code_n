def solve(s: str, k: int) -> int:
    n = len(s)
    zeros = s.count("0")
    if zeros == 0:
        return 0

    def ceil_div(value: int, divisor: int) -> int:
        return (value + divisor - 1) // divisor

    candidates = []
    if zeros % 2 == 0 and k < n:
        operations = max(
            ceil_div(zeros, k),
            ceil_div(zeros, n - k),
        )
        if operations % 2:
            operations += 1
        candidates.append(operations)

    if zeros % 2 == k % 2:
        if k == n:
            if zeros == n:
                candidates.append(1)
        else:
            operations = max(
                ceil_div(zeros, k),
                ceil_div(n - zeros, n - k),
            )
            if operations % 2 == 0:
                operations += 1
            candidates.append(operations)

    return min(candidates, default=-1)
