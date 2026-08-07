class Solution:
    def maxConsecutive(self, bottom: int, top: int, special: List[int]) -> int:
        special.sort()
        answer = special[0] - bottom

        for previous, current in zip(special, special[1:]):
            answer = max(answer, current - previous - 1)

        return max(answer, top - special[-1])
