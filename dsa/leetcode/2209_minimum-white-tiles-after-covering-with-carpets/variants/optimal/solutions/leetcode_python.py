class Solution:
    def minimumWhiteTiles(
        self, floor: str, numCarpets: int, carpetLen: int
    ) -> int:
        length = len(floor)
        previous = [0] * (length + 1)
        for index, tile in enumerate(floor, 1):
            previous[index] = previous[index - 1] + (tile == "1")

        for _ in range(numCarpets):
            current = [0] * (length + 1)
            for index in range(1, length + 1):
                leave_visible = current[index - 1] + (floor[index - 1] == "1")
                cover = previous[max(0, index - carpetLen)]
                current[index] = min(leave_visible, cover)
            previous = current

        return previous[length]
