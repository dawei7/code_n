from typing import List


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        skill_index = {skill: index for index, skill in enumerate(req_skills)}
        full_mask = (1 << len(req_skills)) - 1
        teams = {0: 0}

        for person_index, skills in enumerate(people):
            person_mask = 0
            for skill in skills:
                person_mask |= 1 << skill_index[skill]
            if person_mask == 0:
                continue

            person_bit = 1 << person_index
            for covered, team in list(teams.items()):
                combined = covered | person_mask
                candidate = team | person_bit
                if combined not in teams or candidate.bit_count() < teams[combined].bit_count():
                    teams[combined] = candidate

        selected = teams[full_mask]
        return [index for index in range(len(people)) if selected & (1 << index)]
