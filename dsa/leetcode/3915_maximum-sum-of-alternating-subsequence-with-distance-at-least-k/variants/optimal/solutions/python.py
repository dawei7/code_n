def solve(nums: list[int], k: int) -> int:
    values = sorted(set(nums))
    value_count = len(values)
    rank_of = {value: rank for rank, value in enumerate(values, 1)}
    ranks = [rank_of[value] for value in nums]

    smaller_down = [0] * (value_count + 1)
    larger_up = [0] * (value_count + 1)

    def update(tree: list[int], index: int, score: int) -> None:
        while index <= value_count:
            if score > tree[index]:
                tree[index] = score
            index += index & -index

    def query(tree: list[int], index: int) -> int:
        best = 0
        while index > 0:
            if tree[index] > best:
                best = tree[index]
            index -= index & -index
        return best

    n = len(nums)
    up = [0] * n
    down = [0] * n
    answer = 0

    for index, value in enumerate(nums):
        eligible = index - k
        if eligible >= 0:
            eligible_rank = ranks[eligible]
            update(smaller_down, eligible_rank, down[eligible])
            update(
                larger_up,
                value_count - eligible_rank + 1,
                up[eligible],
            )

        rank = ranks[index]
        up[index] = value + query(smaller_down, rank - 1)
        down[index] = value + query(larger_up, value_count - rank)
        answer = max(answer, up[index], down[index])

    return answer
