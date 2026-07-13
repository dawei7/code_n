class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        position = k - 1
        symbol = 0
        while position:
            symbol ^= position & 1
            position >>= 1
        return symbol
