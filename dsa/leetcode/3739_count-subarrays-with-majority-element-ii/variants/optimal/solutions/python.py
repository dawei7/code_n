def solve(nums: list[int], target: int) -> int:
    n = len(nums)
    offset = n
    frequency = [0] * (2 * n + 1)
    frequency[offset] = 1

    balance = 0
    smaller_prefixes = 0
    answer = 0

    for value in nums:
        if value == target:
            smaller_prefixes += frequency[balance + offset]
            balance += 1
        else:
            balance -= 1
            smaller_prefixes -= frequency[balance + offset]

        answer += smaller_prefixes
        frequency[balance + offset] += 1

    return answer
