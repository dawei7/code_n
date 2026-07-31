class Solution:
    def minimumTime(self, s: str) -> int:
        prefix_cost = 0
        answer = len(s)

        for index, car in enumerate(s):
            if car == "1":
                prefix_cost = min(prefix_cost + 2, index + 1)
            answer = min(answer, prefix_cost + len(s) - index - 1)

        return answer
