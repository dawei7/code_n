class Solution:
    def maximumNumberOfOnes(
        self, width: int, height: int, sideLength: int, maxOnes: int
    ) -> int:
        row_counts = [
            (height - 1 - residue) // sideLength + 1
            for residue in range(sideLength)
        ]
        column_counts = [
            (width - 1 - residue) // sideLength + 1
            for residue in range(sideLength)
        ]
        frequencies = [
            row_count * column_count
            for row_count in row_counts
            for column_count in column_counts
        ]
        frequencies.sort(reverse=True)
        return sum(frequencies[:maxOnes])
