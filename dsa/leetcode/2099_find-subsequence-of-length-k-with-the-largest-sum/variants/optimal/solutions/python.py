def solve(nums: list[int], k: int) -> list[int]:
    selected_indices = sorted(
        range(len(nums)),
        key=lambda index: nums[index],
        reverse=True,
    )[:k]
    selected_indices.sort()
    return [nums[index] for index in selected_indices]
