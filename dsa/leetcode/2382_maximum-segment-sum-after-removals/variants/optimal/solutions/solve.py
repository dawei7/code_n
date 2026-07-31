def solve(nums: list[int], removeQueries: list[int]) -> list[int]:
    n = len(nums)
    parent = list(range(n))
    segment_sum = [0] * n
    active = [False] * n
    answer = [0] * n

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    def union(first: int, second: int) -> None:
        first_root = find(first)
        second_root = find(second)
        if first_root == second_root:
            return
        parent[second_root] = first_root
        segment_sum[first_root] += segment_sum[second_root]

    maximum = 0
    for query_index in range(n - 1, -1, -1):
        answer[query_index] = maximum
        index = removeQueries[query_index]
        active[index] = True
        segment_sum[index] = nums[index]

        if index > 0 and active[index - 1]:
            union(index, index - 1)
        if index + 1 < n and active[index + 1]:
            union(index, index + 1)

        maximum = max(maximum, segment_sum[find(index)])

    return answer
