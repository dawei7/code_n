from collections import Counter


def solve(nums: list[int], k: int) -> list[int]:
    frequencies = Counter(nums[:k])
    answer = [len(frequencies)]

    for right in range(k, len(nums)):
        outgoing = nums[right - k]
        frequencies[outgoing] -= 1
        if frequencies[outgoing] == 0:
            del frequencies[outgoing]

        frequencies[nums[right]] += 1
        answer.append(len(frequencies))

    return answer
