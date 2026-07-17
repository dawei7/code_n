class Solution:
    def checkPalindromeFormation(self, a: str, b: str) -> bool:
        def is_palindrome(value: str, left: int, right: int) -> bool:
            while left < right:
                if value[left] != value[right]:
                    return False
                left += 1
                right -= 1
            return True

        def can_combine(prefix_source: str, suffix_source: str) -> bool:
            left = 0
            right = len(prefix_source) - 1
            while left < right and prefix_source[left] == suffix_source[right]:
                left += 1
                right -= 1
            return is_palindrome(prefix_source, left, right) or is_palindrome(
                suffix_source, left, right
            )

        return can_combine(a, b) or can_combine(b, a)
