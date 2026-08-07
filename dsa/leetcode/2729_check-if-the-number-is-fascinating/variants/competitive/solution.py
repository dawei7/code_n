class Solution:
    def isFascinating(self, n: int) -> bool:
        digits = f"{n}{2 * n}{3 * n}"
        return len(digits) == 9 and set(digits) == set("123456789")
