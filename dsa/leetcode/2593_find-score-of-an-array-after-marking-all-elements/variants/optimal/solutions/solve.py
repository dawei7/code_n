def solve(nums: list[int]) -> int:
    marked = [False] * len(nums)
    score = 0

    for value, index in sorted((value, index) for index, value in enumerate(nums)):
        if marked[index]:
            continue

        score += value
        marked[index] = True
        if index > 0:
            marked[index - 1] = True
        if index + 1 < len(nums):
            marked[index + 1] = True

    return score
