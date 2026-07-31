class Solution:
    def countKeyChanges(self, s: str) -> int:
        return sum(left.lower() != right.lower() for left, right in zip(s, s[1:]))
