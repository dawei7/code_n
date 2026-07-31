from typing import List


def solve(nums: List[int], queries: List[List[int]]) -> List[int]:
    ordered = sorted((value, index) for index, value in enumerate(nums))
    marked = [False] * len(nums)
    remaining_sum = sum(nums)
    cursor = 0
    answer = []

    for index, count in queries:
        if not marked[index]:
            marked[index] = True
            remaining_sum -= nums[index]

        while count > 0 and cursor < len(ordered):
            value, smallest_index = ordered[cursor]
            cursor += 1

            if marked[smallest_index]:
                continue

            marked[smallest_index] = True
            remaining_sum -= value
            count -= 1

        answer.append(remaining_sum)

    return answer
