class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = blocks[:k].count("W")
        answer = white_count

        for right in range(k, len(blocks)):
            if blocks[right - k] == "W":
                white_count -= 1
            if blocks[right] == "W":
                white_count += 1
            answer = min(answer, white_count)

        return answer
