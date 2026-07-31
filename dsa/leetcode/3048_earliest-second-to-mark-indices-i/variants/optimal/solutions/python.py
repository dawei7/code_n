def solve(nums: list[int], changeIndices: list[int]) -> int:
    index_count = len(nums)

    def can_finish(seconds: int) -> bool:
        last_occurrence = [-1] * index_count
        for second in range(seconds):
            last_occurrence[changeIndices[second] - 1] = second

        if -1 in last_occurrence:
            return False

        available_decrements = 0
        for second in range(seconds):
            index = changeIndices[second] - 1
            if second == last_occurrence[index]:
                if available_decrements < nums[index]:
                    return False
                available_decrements -= nums[index]
            else:
                available_decrements += 1

        return True

    left = 1
    right = len(changeIndices)
    answer = -1

    while left <= right:
        middle = (left + right) // 2
        if can_finish(middle):
            answer = middle
            right = middle - 1
        else:
            left = middle + 1

    return answer
