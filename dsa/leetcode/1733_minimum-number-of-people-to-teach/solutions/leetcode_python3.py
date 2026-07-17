from typing import List


class Solution:
    def minimumTeachings(
        self,
        n: int,
        languages: List[List[int]],
        friendships: List[List[int]],
    ) -> int:
        del n
        known = [set(values) for values in languages]
        affected = set()

        for first, second in friendships:
            first -= 1
            second -= 1
            if known[first].isdisjoint(known[second]):
                affected.add(first)
                affected.add(second)

        if not affected:
            return 0

        frequency = {}
        for person in affected:
            for language in known[person]:
                frequency[language] = frequency.get(language, 0) + 1

        return len(affected) - max(frequency.values())
