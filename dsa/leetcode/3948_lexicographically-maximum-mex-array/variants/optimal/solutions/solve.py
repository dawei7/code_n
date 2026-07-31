def solve(nums: list[int]) -> list[int]:
    n = len(nums)
    remaining = [0] * (n + 1)
    for value in nums:
        if value <= n:
            remaining[value] += 1

    mex = 0
    while remaining[mex] > 0:
        mex += 1

    result = []
    index = 0
    while index < n:
        if mex == 0:
            value = nums[index]
            if value <= n:
                remaining[value] -= 1
            result.append(0)
            index += 1
            continue

        segment_mex = mex
        unseen = segment_mex
        seen = set()
        while unseen > 0:
            value = nums[index]
            if value <= n:
                remaining[value] -= 1
            if value < segment_mex and value not in seen:
                seen.add(value)
                unseen -= 1
            index += 1

        result.append(segment_mex)
        mex = 0
        while remaining[mex] > 0:
            mex += 1

    return result
