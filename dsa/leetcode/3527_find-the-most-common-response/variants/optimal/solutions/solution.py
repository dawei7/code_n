class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        frequency = {}

        for day in responses:
            for response in set(day):
                frequency[response] = frequency.get(response, 0) + 1

        return min(frequency, key=lambda response: (-frequency[response], response))
