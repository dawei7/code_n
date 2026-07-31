class Solution:
    def minMovesToCaptureTheQueen(
        self,
        a: int,
        b: int,
        c: int,
        d: int,
        e: int,
        f: int,
    ) -> int:
        def between(left: int, middle: int, right: int) -> bool:
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
