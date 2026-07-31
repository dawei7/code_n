def solve(nums: list[int], x: int) -> int:
    prefix = [0]
    for number in nums:
        prefix.append(prefix[-1] + number)

    answer = 0
    power = 1
    while x * power <= prefix[-1]:
        lower = x * power
        upper = (x + 1) * power - 1
        residue_counts = [0] * 10
        add = 0
        remove = 0

        for right in prefix[1:]:
            while add < len(prefix) and prefix[add] <= right - lower:
                residue_counts[prefix[add] % 10] += 1
                add += 1
            while remove < add and prefix[remove] < right - upper:
                residue_counts[prefix[remove] % 10] -= 1
                remove += 1

            answer += residue_counts[(right - x) % 10]

        power *= 10

    return answer
