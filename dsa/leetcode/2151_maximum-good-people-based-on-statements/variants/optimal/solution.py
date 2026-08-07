from typing import List


class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        people = len(statements)
        maximum = 0

        for mask in range(1 << people):
            consistent = True
            for person in range(people):
                if not (mask >> person) & 1:
                    continue
                for target, statement in enumerate(statements[person]):
                    if statement != 2 and statement != ((mask >> target) & 1):
                        consistent = False
                        break
                if not consistent:
                    break
            if consistent:
                maximum = max(maximum, mask.bit_count())

        return maximum
