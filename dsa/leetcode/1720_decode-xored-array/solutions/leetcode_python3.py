from typing import List


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        decoded = [first]
        for value in encoded:
            decoded.append(decoded[-1] ^ value)
        return decoded
