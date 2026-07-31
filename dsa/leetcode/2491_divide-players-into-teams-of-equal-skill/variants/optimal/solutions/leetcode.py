from typing import List


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        target = skill[0] + skill[-1]
        chemistry = 0

        for left in range(len(skill) // 2):
            right = len(skill) - 1 - left
            if skill[left] + skill[right] != target:
                return -1
            chemistry += skill[left] * skill[right]

        return chemistry
