from typing import List


class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        n = len(dict)
        m = len(dict[0])
        MOD = (1 << 61) - 1
        BASE = 27

        hashes = []
        for word in dict:
            h = 0
            for ch in word:
                h = (h * BASE + (ord(ch) - 96)) % MOD
            hashes.append(h)

        power = 1
        for j in range(m - 1, -1, -1):
            seen = set()
            for i in range(n):
                ch_val = ord(dict[i][j]) - 96
                h_without = (hashes[i] - ch_val * power) % MOD
                if h_without in seen:
                    return True
                seen.add(h_without)
            power = (power * BASE) % MOD

        return False

