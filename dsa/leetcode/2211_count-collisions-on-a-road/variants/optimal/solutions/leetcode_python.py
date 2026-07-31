class Solution:
    def countCollisions(self, directions: str) -> int:
        trapped = directions.lstrip("L").rstrip("R")
        return len(trapped) - trapped.count("S")
