class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        left = 0
        right = 0
        length = len(start)

        while True:
            while left < length and start[left] == "X":
                left += 1
            while right < length and end[right] == "X":
                right += 1

            if left == length or right == length:
                return left == length and right == length
            if start[left] != end[right]:
                return False
            if start[left] == "L" and left < right:
                return False
            if start[left] == "R" and left > right:
                return False

            left += 1
            right += 1
