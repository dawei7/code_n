class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        parity = 0
        for value in derived:
            parity ^= value
        return parity == 0
