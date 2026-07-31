def solve(s: str, order: list[int], k: int) -> int:
    n = len(s)
    total_substrings = n * (n + 1) // 2
    if total_substrings < k:
        return -1

    activation_time = [0] * n
    for time, index in enumerate(order):
        activation_time[index] = time

    def is_active(time: int) -> bool:
        invalid = 0
        inactive_run = 0
        for activated_at in activation_time:
            if activated_at <= time:
                invalid += inactive_run * (inactive_run + 1) // 2
                inactive_run = 0
            else:
                inactive_run += 1
        invalid += inactive_run * (inactive_run + 1) // 2
        return total_substrings - invalid >= k

    left = 0
    right = n - 1
    while left < right:
        middle = (left + right) // 2
        if is_active(middle):
            right = middle
        else:
            left = middle + 1
    return left

