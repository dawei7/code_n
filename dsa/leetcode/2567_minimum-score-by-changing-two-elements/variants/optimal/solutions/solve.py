from heapq import nlargest, nsmallest


def solve(nums: list[int]) -> int:
    smallest = nsmallest(3, nums)
    largest = nlargest(3, nums)

    return min(
        largest[2] - smallest[0],
        largest[1] - smallest[1],
        largest[0] - smallest[2],
    )
