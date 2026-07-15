class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        current_cost = 0
        best = 0
        for right, (source, target) in enumerate(zip(s, t)):
            current_cost += abs(ord(source) - ord(target))
            while current_cost > maxCost:
                current_cost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
            best = max(best, right - left + 1)
        return best
