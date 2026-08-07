class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x = 0
        y = 0
        answer = 0

        for length, direction in enumerate(s, 1):
            if direction == "N":
                y += 1
            elif direction == "S":
                y -= 1
            elif direction == "E":
                x += 1
            else:
                x -= 1

            answer = max(answer, min(length, abs(x) + abs(y) + 2 * k))

        return answer
