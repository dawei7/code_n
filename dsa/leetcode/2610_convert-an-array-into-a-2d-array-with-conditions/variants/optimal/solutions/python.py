from typing import List


def solve(nums: List[int]) -> List[List[int]]:
    frequency = {}
    rows = []

    for number in nums:
        occurrence = frequency.get(number, 0)
        if occurrence == len(rows):
            rows.append([])
        rows[occurrence].append(number)
        frequency[number] = occurrence + 1

    return rows
