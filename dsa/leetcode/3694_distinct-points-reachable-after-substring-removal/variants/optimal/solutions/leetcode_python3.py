class Solution:
    def distinctPoints(self, s: str, k: int) -> int:
        movement = {
            "U": (0, 1),
            "D": (0, -1),
            "L": (-1, 0),
            "R": (1, 0),
        }

        removed_x = 0
        removed_y = 0
        for direction in s[:k]:
            dx, dy = movement[direction]
            removed_x += dx
            removed_y += dy

        removed_displacements = {(removed_x, removed_y)}
        for right in range(k, len(s)):
            entering_x, entering_y = movement[s[right]]
            leaving_x, leaving_y = movement[s[right - k]]
            removed_x += entering_x - leaving_x
            removed_y += entering_y - leaving_y
            removed_displacements.add((removed_x, removed_y))

        return len(removed_displacements)
