def solve(nums: list[int], threshold: list[int]) -> int:
    releases = {}
    for value, required_step in zip(nums, threshold):
        count, total = releases.get(required_step, (0, 0))
        releases[required_step] = (count + 1, total + value)

    unused_released = 0
    released_total = 0
    for step in range(1, len(nums) + 1):
        count, total = releases.get(step, (0, 0))
        unused_released += count
        released_total += total
        if unused_released == 0:
            break
        unused_released -= 1
    return released_total
