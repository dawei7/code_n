class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        active = 0
        best_gain = 0
        previous_zeros = 0
        index = 0

        while index < len(s):
            if s[index] == "1":
                active += 1
                index += 1
                continue

            end = index
            while end < len(s) and s[end] == "0":
                end += 1
            zeros = end - index
            if previous_zeros:
                best_gain = max(best_gain, previous_zeros + zeros)
            previous_zeros = zeros
            index = end

        return active + best_gain
