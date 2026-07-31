from heapq import heappop, heappush


class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        available = []
        difference = [0] * (len(nums) + 1)
        coverage = 0
        selected = 0
        query_index = 0

        for index, required in enumerate(nums):
            coverage += difference[index]

            while query_index < len(queries) and queries[query_index][0] <= index:
                heappush(available, -queries[query_index][1])
                query_index += 1

            while coverage < required:
                if not available or -available[0] < index:
                    return -1

                end = -heappop(available)
                coverage += 1
                difference[end + 1] -= 1
                selected += 1

        return len(queries) - selected

