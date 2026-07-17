def solve(nums: list[int], limit: int) -> int:
    difference = [0] * (2 * limit + 2)

    for index in range(len(nums) // 2):
        first = nums[index]
        second = nums[-1 - index]
        low = 1 + min(first, second)
        exact = first + second
        high = limit + max(first, second)

        difference[2] += 2
        difference[low] -= 1
        difference[exact] -= 1
        difference[exact + 1] += 1
        difference[high + 1] += 1

    answer = len(nums)
    moves = 0
    for target in range(2, 2 * limit + 1):
        moves += difference[target]
        answer = min(answer, moves)
    return answer
