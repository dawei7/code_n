def solve(nums: list[int], pivot: int) -> list[int]:
    smaller: list[int] = []
    equal: list[int] = []
    greater: list[int] = []

    for value in nums:
        if value < pivot:
            smaller.append(value)
        elif value == pivot:
            equal.append(value)
        else:
            greater.append(value)

    return smaller + equal + greater
