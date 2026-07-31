from typing import List


def solve(nums: List[int], operations: List[List[int]]) -> List[int]:
    result = list(nums)
    indices = {value: index for index, value in enumerate(result)}

    for old_value, new_value in operations:
        index = indices.pop(old_value)
        result[index] = new_value
        indices[new_value] = index

    return result
