from typing import List


class Solution:
    def smallestTrimmedNumbers(
        self, nums: List[str], queries: List[List[int]]
    ) -> List[int]:
        by_trim: List[List[tuple[int, int]]] = [
            [] for _ in range(max(trim for _, trim in queries) + 1)
        ]
        for query_index, (rank, trim) in enumerate(queries):
            by_trim[trim].append((query_index, rank))

        order = list(range(len(nums)))
        answer = [0] * len(queries)
        for trim in range(1, len(by_trim)):
            buckets: List[List[int]] = [[] for _ in range(10)]
            position = -trim
            for index in order:
                buckets[ord(nums[index][position]) - ord("0")].append(index)
            order = [index for bucket in buckets for index in bucket]

            for query_index, rank in by_trim[trim]:
                answer[query_index] = order[rank - 1]

        return answer
