def solve(s: str) -> int:
    length = len(s)
    radius = [0] * length
    left = 0
    right = -1

    for center in range(length):
        current = (
            1
            if center > right
            else min(radius[left + right - center], right - center + 1)
        )

        while (
            center - current >= 0
            and center + current < length
            and s[center - current] == s[center + current]
        ):
            current += 1

        radius[center] = current
        if center + current - 1 > right:
            left = center - current + 1
            right = center + current - 1

    ending = [0] * length
    starting = [0] * length

    for center, current in enumerate(radius):
        palindrome_length = 2 * current - 1
        ending[center + current - 1] = max(
            ending[center + current - 1],
            palindrome_length,
        )
        starting[center - current + 1] = max(
            starting[center - current + 1],
            palindrome_length,
        )

    for index in range(length - 2, -1, -1):
        ending[index] = max(ending[index], ending[index + 1] - 2)
    for index in range(1, length):
        ending[index] = max(ending[index], ending[index - 1])

    for index in range(1, length):
        starting[index] = max(starting[index], starting[index - 1] - 2)
    for index in range(length - 2, -1, -1):
        starting[index] = max(starting[index], starting[index + 1])

    return max(
        ending[index] * starting[index + 1]
        for index in range(length - 1)
    )
