class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        squares = [value * value for value in range(1, int(n**0.5) + 1)]
        winning = bytearray(n + 1)
        for stones in range(1, n + 1):
            for square in squares:
                if square > stones:
                    break
                if not winning[stones - square]:
                    winning[stones] = 1
                    break
        return bool(winning[n])
