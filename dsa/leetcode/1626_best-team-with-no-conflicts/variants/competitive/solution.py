from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = sorted(zip(ages, scores))
        ordered_scores = sorted(set(scores))
        score_rank = {score: index + 1 for index, score in enumerate(ordered_scores)}
        tree = [0] * (len(ordered_scores) + 1)

        answer = 0
        for _, score in players:
            index = score_rank[score]
            best_prefix = 0
            cursor = index
            while cursor > 0:
                best_prefix = max(best_prefix, tree[cursor])
                cursor -= cursor & -cursor

            team_score = best_prefix + score
            answer = max(answer, team_score)
            cursor = index
            while cursor < len(tree):
                tree[cursor] = max(tree[cursor], team_score)
                cursor += cursor & -cursor
        return answer
