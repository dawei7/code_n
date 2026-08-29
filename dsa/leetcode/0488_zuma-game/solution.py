import collections
import re


class Solution:
    def findMinStep(self, board: str, hand: str) -> int:
        def clean(s: str) -> str:
            i = 0
            while i < len(s):
                j = i
                while j < len(s) and s[j] == s[i]:
                    j += 1
                if j - i >= 3:
                    return clean(s[:i] + s[j:])
                i = j
            return s

        hand = "".join(sorted(hand))
        q = collections.deque([(board, hand, 0)])
        visited = set([(board, hand)])

        while q:
            curr_board, curr_hand, steps = q.popleft()
            if not curr_board:
                return steps

            hand_chars = set(curr_hand)
            for c in hand_chars:
                c_idx = curr_hand.index(c)
                next_hand = curr_hand[:c_idx] + curr_hand[c_idx + 1 :]

                for i in range(len(curr_board) + 1):
                    same_as_curr = i < len(curr_board) and curr_board[i] == c
                    between_same = (
                        0 < i < len(curr_board)
                        and curr_board[i - 1] == curr_board[i]
                        and curr_board[i] != c
                    )
                    if not (same_as_curr or between_same):
                        continue

                    new_board = clean(curr_board[:i] + c + curr_board[i:])
                    if (new_board, next_hand) not in visited:
                        visited.add((new_board, next_hand))
                        q.append((new_board, next_hand, steps + 1))
        return -1

