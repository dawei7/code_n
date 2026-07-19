class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        needed = 1 << k
        if len(s) - k + 1 < needed:
            return False

        seen = bytearray(needed)
        mask = needed - 1
        window = 0
        remaining = needed

        for index, character in enumerate(s):
            window = ((window << 1) & mask) | (character == "1")
            if index >= k - 1 and not seen[window]:
                seen[window] = 1
                remaining -= 1
                if remaining == 0:
                    return True

        return False
