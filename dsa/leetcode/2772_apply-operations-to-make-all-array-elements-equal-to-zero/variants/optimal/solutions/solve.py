def solve(nums: list[int], k: int) -> bool:
    expiration = [0] * (len(nums) + 1)
    active_decrements = 0

    for index, value in enumerate(nums):
        active_decrements -= expiration[index]
        required = value - active_decrements

        if required < 0:
            return False
        if required == 0:
            continue
        if index + k > len(nums):
            return False

        active_decrements += required
        expiration[index + k] += required

    return True
