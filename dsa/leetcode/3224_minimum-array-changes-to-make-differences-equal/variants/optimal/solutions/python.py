def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    # diff_counts stores the frequency of absolute differences of pairs
    diff_counts = [0] * (k + 1)
    # diff_array for sweep-line:
    # change_needed[x] = (count of pairs needing 2 changes) + (count of pairs needing 1 change)
    # We use a difference array to calculate this efficiently.
    # Base cost: every pair needs at least 1 change if target x != abs(a-b)
    # If x <= max_possible_diff, we can achieve it with 1 change.
    # If x > max_possible_diff, we need 2 changes.

    # diff_array[i] stores the change in the number of operations needed at difference i
    diff_array = [0] * (k + 2)

    for i in range(n // 2):
        a, b = nums[i], nums[n - 1 - i]
        diff = abs(a - b)
        diff_counts[diff] += 1

        # Max difference achievable with 1 change
        max_diff = max(max(a, b), k - min(a, b))

        # For a target x:
        # If x == diff: 0 changes
        # If x <= max_diff: 1 change
        # If x > max_diff: 2 changes

        # Start with 2 changes for all x.
        diff_array[0] += 2
        # If x <= max_diff, we only need 1 change.
        diff_array[0] -= 1
        diff_array[max_diff + 1] += 1
        # If x == diff, we need 0 changes (so subtract 1 more)
        diff_array[diff] -= 1
        diff_array[diff + 1] += 1

    min_ops = float('inf')
    current_ops = 0
    for x in range(k + 1):
        current_ops += diff_array[x]
        min_ops = min(min_ops, current_ops)

    return int(min_ops)
