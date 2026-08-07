# The rand7() API is already defined for you by LeetCode.
class Solution:
    def rand10(self) -> int:
        while True:
            cell = (rand7() - 1) * 7 + rand7()
            if cell <= 40:
                return 1 + (cell - 1) % 10
