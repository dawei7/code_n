from typing import List


class Solution:
    def catchMaximumAmountofPeople(self, team: List[int], dist: int) -> int:
        catchers = [index for index, value in enumerate(team) if value == 1]
        people = [index for index, value in enumerate(team) if value == 0]
        catcher_index = 0
        person_index = 0
        caught = 0

        while catcher_index < len(catchers) and person_index < len(people):
            catcher = catchers[catcher_index]
            person = people[person_index]
            if person < catcher - dist:
                person_index += 1
            elif catcher < person - dist:
                catcher_index += 1
            else:
                caught += 1
                catcher_index += 1
                person_index += 1

        return caught
