from typing import List


def solve(a: List[str], b: List[str]) -> bool:
    greatest = [[None] * 26 for _ in range(2)]
    for player, words in enumerate((a, b)):
        for word in words:
            greatest[player][ord(word[0]) - ord("a")] = word

    memo = {}

    def can_win(player: int, last: str) -> bool:
        state = (player, last)
        if state in memo:
            return memo[state]

        letter = ord(last[0]) - ord("a")
        for next_letter in (letter, letter + 1):
            if next_letter == 26:
                continue
            word = greatest[player][next_letter]
            if word is not None and word > last:
                if not can_win(1 - player, word):
                    memo[state] = True
                    return True

        memo[state] = False
        return False

    return not can_win(1, a[0])
