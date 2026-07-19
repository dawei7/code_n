def solve(nums: list[int], min_k: int, max_k: int) -> int:
    ans = 0
    bad_idx = -1
    min_idx = -1
    max_idx = -1

    for i, x in enumerate(nums):
        # If the current number is outside the allowed range,
        # it resets the potential window.
        if not (min_k <= x <= max_k):
            bad_idx = i

        # Update the last seen positions of min_k and max_k
        if x == min_k:
            min_idx = i
        if x == max_k:
            max_idx = i

        # The number of valid subarrays ending at i is determined by the
        # distance between the closest boundary (min or max) and the
        # last 'bad' index.
        count = min(min_idx, max_idx) - bad_idx
        if count > 0:
            ans += count

    return ans
