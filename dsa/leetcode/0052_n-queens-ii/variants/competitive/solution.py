class Solution:
    def totalNQueens(self, n: int) -> int:
        board_mask = (1 << n) - 1

        def count(columns: int, descending: int, ascending: int) -> int:
            if columns == board_mask:
                return 1

            total = 0
            free = board_mask & ~(columns | descending | ascending)
            while free:
                bit = free & -free
                free -= bit
                total += count(
                    columns | bit,
                    ((descending | bit) << 1) & board_mask,
                    (ascending | bit) >> 1,
                )
            return total

        return count(0, 0, 0)
