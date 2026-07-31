class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()
        left = 0
        covered = 0
        answer = 0

        for right, (start, end) in enumerate(tiles):
            covered += end - start + 1
            carpet_start = end - carpetLen + 1

            while tiles[left][1] < carpet_start:
                covered -= tiles[left][1] - tiles[left][0] + 1
                left += 1

            uncovered_left = max(0, carpet_start - tiles[left][0])
            answer = max(answer, covered - uncovered_left)
            if answer == carpetLen:
                return answer

        return answer
