from typing import List


class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        suffix = [0] * k
        answer = -(10**18)

        for index in range(len(energy) - 1, -1, -1):
            residue = index % k
            total = energy[index] + suffix[residue]
            suffix[residue] = total
            answer = max(answer, total)

        return answer
