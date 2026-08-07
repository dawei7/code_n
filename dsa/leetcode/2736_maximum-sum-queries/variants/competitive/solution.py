class Solution:
    def maximumSumQueries(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        from bisect import bisect_left

        values = sorted(set(nums2))
        size = len(values)
        tree = [-1] * (size + 1)

        def update(index, value):
            while index <= size:
                tree[index] = max(tree[index], value)
                index += index & -index

        def prefix_max(index):
            result = -1
            while index > 0:
                result = max(result, tree[index])
                index -= index & -index
            return result

        points = sorted(zip(nums1, nums2), reverse=True)
        ordered_queries = sorted(
            ((x, y, index) for index, (x, y) in enumerate(queries)),
            reverse=True,
        )
        answers = [-1] * len(queries)
        point_index = 0

        for x, y, query_index in ordered_queries:
            while point_index < len(points) and points[point_index][0] >= x:
                a, b = points[point_index]
                reversed_index = size - bisect_left(values, b)
                update(reversed_index, a + b)
                point_index += 1

            eligible_count = size - bisect_left(values, y)
            answers[query_index] = prefix_max(eligible_count)

        return answers
