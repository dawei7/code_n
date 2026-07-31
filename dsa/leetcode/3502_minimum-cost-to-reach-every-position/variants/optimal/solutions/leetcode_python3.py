class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        answer = []
        best = cost[0]

        for value in cost:
            best = min(best, value)
            answer.append(best)

        return answer
