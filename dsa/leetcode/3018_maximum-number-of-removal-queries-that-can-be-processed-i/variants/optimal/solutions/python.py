def solve(nums: list[int], queries: list[int]) -> int:
    query_count = len(queries)
    current = [0]
    answer = 0

    for length in range(len(nums), 0, -1):
        following = [-1] * (len(current) + 1)

        for left, processed in enumerate(current):
            if processed < 0:
                continue

            right = left + length - 1
            answer = max(answer, processed)
            take_left = processed + int(
                processed < query_count and nums[left] >= queries[processed]
            )
            take_right = processed + int(
                processed < query_count and nums[right] >= queries[processed]
            )

            following[left + 1] = max(following[left + 1], processed, take_left)
            following[left] = max(following[left], processed, take_right)

        current = following

    return max(answer, max(current))
