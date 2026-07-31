class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        component = [0] * n

        for index in range(1, n):
            component[index] = component[index - 1]
            if nums[index] - nums[index - 1] > maxDiff:
                component[index] += 1

        return [component[source] == component[target] for source, target in queries]
