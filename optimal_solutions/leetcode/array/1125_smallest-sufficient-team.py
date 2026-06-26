"""Optimal solution for LeetCode 1125: Smallest Sufficient Team."""


def solve(req_skills: list[str], people: list[list[str]]) -> list[int]:
    skill_index = {skill: i for i, skill in enumerate(req_skills)}
    full = (1 << len(req_skills)) - 1
    dp: dict[int, list[int]] = {0: []}

    for i, skills in enumerate(people):
        mask = 0
        for skill in skills:
            mask |= 1 << skill_index[skill]
        if mask == 0:
            continue
        for current, team in list(dp.items()):
            combined = current | mask
            if combined not in dp or len(team) + 1 < len(dp[combined]):
                dp[combined] = team + [i]
    return dp[full]
