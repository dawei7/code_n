def solve(nums: list[int]) -> int:
    previous = nums[0]
    features = 0

    for current, following in zip(nums[1:], nums[2:]):
        if current == following:
            continue
        if (current > previous and current > following) or (
            current < previous and current < following
        ):
            features += 1
        previous = current

    return features
