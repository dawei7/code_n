


def solve():
    class Solution:
        def __init__(self):
            self.rows = [0] * 9
            self.cols = [0] * 9
            self.boxes = [0] * 9

        def backtrack(self, board) -> bool:
            best_row, best_col = -1, -1
            max_popcount = -1
            best_box_idx = -1
            best_mask = 0

            for r in range(9):
                for c in range(9):
                    if board[r][c] == '.':
                        box_idx = (r // 3) * 3 + (c // 3)
                        combined_mask = self.rows[r] | self.cols[c] | self.boxes[box_idx]
                        pop = bin(combined_mask).count('1')
                        if pop > max_popcount:
                            max_popcount = pop
                            best_row = r
                            best_col = c
                            best_box_idx = box_idx
                            best_mask = combined_mask

            if best_row == -1:
                return True
            if max_popcount == 9:
                return False

            candidates = ~best_mask & 0x1FF
            while candidates > 0:
                lsb = candidates & -candidates
                candidates ^= lsb
                num = (lsb).bit_length() - 1

                mask = 1 << num
                self.rows[best_row] |= mask
                self.cols[best_col] |= mask
                self.boxes[best_box_idx] |= mask
                board[best_row][best_col] = str(num + 1)

                if self.backtrack(board):
                    return True

                self.rows[best_row] &= ~mask
                self.cols[best_col] &= ~mask
                self.boxes[best_box_idx] &= ~mask
                board[best_row][best_col] = '.'

            return False

        def solvePuzzle(self, board) -> None:
            self.rows = [0] * 9
            self.cols = [0] * 9
            self.boxes = [0] * 9

            for r in range(9):
                for c in range(9):
                    if board[r][c] != '.':
                        num = int(board[r][c]) - 1
                        mask = 1 << num
                        box_idx = (r // 3) * 3 + (c // 3)
                        self.rows[r] |= mask
                        self.cols[c] |= mask
                        self.boxes[box_idx] |= mask

            self.backtrack(board)


if __name__ == "__main__":
    solve()
