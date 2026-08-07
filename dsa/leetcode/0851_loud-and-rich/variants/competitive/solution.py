from typing import List


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        richer_people = [[] for _ in quiet]
        for rich, poor in richer:
            richer_people[poor].append(rich)

        answer = [-1] * len(quiet)

        def quietest(person: int) -> int:
            if answer[person] != -1:
                return answer[person]

            answer[person] = person
            for richer_person in richer_people[person]:
                candidate = quietest(richer_person)
                if quiet[candidate] < quiet[answer[person]]:
                    answer[person] = candidate
            return answer[person]

        for person in range(len(quiet)):
            quietest(person)

        return answer
