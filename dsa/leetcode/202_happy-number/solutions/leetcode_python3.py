class Solution:
    def isHappy(self, n: int) -> bool:
        def next_value(number: int) -> int:
            total = 0
            while number:
                number, digit = divmod(number, 10)
                total += digit * digit
            return total

        slow, fast = n, next_value(n)
        while slow != fast:
            slow = next_value(slow)
            fast = next_value(next_value(fast))
        return slow == 1
