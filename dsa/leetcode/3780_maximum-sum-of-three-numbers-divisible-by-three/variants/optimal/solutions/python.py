def solve(nums: list[int]) -> int:
    largest = [[], [], []]
    for value in nums:
        bucket = largest[value % 3]
        bucket.append(value)
        bucket.sort(reverse=True)
        if len(bucket) > 3:
            bucket.pop()

    answer = 0
    for counts in ((3, 0, 0), (0, 3, 0), (0, 0, 3), (1, 1, 1)):
        if all(len(largest[remainder]) >= count for remainder, count in enumerate(counts)):
            candidate = sum(
                sum(largest[remainder][:count])
                for remainder, count in enumerate(counts)
            )
            answer = max(answer, candidate)
    return answer
