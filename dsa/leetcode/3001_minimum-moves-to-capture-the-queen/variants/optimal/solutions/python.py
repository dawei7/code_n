def solve(a, b, c, d, e, f):
    def between(left, middle, right):
        return min(left, right) < middle < max(left, right)

    rook_attacks = (
        a == e and not (c == a and between(b, d, f))
    ) or (
        b == f and not (d == b and between(a, c, e))
    )

    bishop_line = abs(c - e) == abs(d - f)
    rook_blocks_bishop = bishop_line and between(c, a, e) and (
        c - d == e - f == a - b or c + d == e + f == a + b
    )

    return 1 if rook_attacks or (bishop_line and not rook_blocks_bishop) else 2
