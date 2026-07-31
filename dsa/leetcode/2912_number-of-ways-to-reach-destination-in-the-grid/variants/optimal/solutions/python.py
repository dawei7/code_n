def solve(n: int, m: int, k: int, source: list[int], dest: list[int]) -> int:
    mod = 1_000_000_007

    at_dest = int(source[0] == dest[0] and source[1] == dest[1])
    same_row = int(source[0] == dest[0] and source[1] != dest[1])
    same_col = int(source[0] != dest[0] and source[1] == dest[1])
    neither = int(source[0] != dest[0] and source[1] != dest[1])

    for _ in range(k):
        at_dest, same_row, same_col, neither = (
            (same_row + same_col) % mod,
            (at_dest * (m - 1) + same_row * (m - 2) + neither) % mod,
            (at_dest * (n - 1) + same_col * (n - 2) + neither) % mod,
            (
                same_row * (n - 1)
                + same_col * (m - 1)
                + neither * (n + m - 4)
            )
            % mod,
        )

    return at_dest
