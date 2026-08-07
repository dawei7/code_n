class Solution:
    def minimumCost(self, m: int, n: int, horizontalCut: List[int], verticalCut: List[int]) -> int:
        horizontalCut.sort(reverse=True)
        verticalCut.sort(reverse=True)
        horizontal_index = vertical_index = 0
        horizontal_pieces = vertical_pieces = 1
        total = 0

        while horizontal_index < len(horizontalCut) and vertical_index < len(verticalCut):
            if horizontalCut[horizontal_index] >= verticalCut[vertical_index]:
                total += horizontalCut[horizontal_index] * vertical_pieces
                horizontal_pieces += 1
                horizontal_index += 1
            else:
                total += verticalCut[vertical_index] * horizontal_pieces
                vertical_pieces += 1
                vertical_index += 1

        while horizontal_index < len(horizontalCut):
            total += horizontalCut[horizontal_index] * vertical_pieces
            horizontal_index += 1
        while vertical_index < len(verticalCut):
            total += verticalCut[vertical_index] * horizontal_pieces
            vertical_index += 1
        return total
