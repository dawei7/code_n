from collections import deque


class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        limit = 2**31 - 1
        digits = sorted({digit1, digit2})
        queue = deque(digit for digit in digits if digit != 0)

        while queue:
            value = queue.popleft()
            if value > k and value % k == 0:
                return value

            for digit in digits:
                following = value * 10 + digit
                if following <= limit:
                    queue.append(following)

        return -1
