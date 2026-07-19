def solve(stones: list[int]) -> int:
    n = len(stones)
    prefix = [0]
    for value in stones:
        prefix.append(prefix[-1] + value)

    advantage = [0] * n
    for length in range(2, n + 1):
        for left in range(n - length + 1):
            right = left + length - 1
            remove_left = (
                prefix[right + 1] - prefix[left + 1] - advantage[left + 1]
            )
            remove_right = prefix[right] - prefix[left] - advantage[left]
            advantage[left] = max(remove_left, remove_right)

    return advantage[0]
