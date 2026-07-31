def solve(nums: list[int], key: int) -> int:
    follower_counts = [0] * 1001
    answer = 0

    for index in range(len(nums) - 1):
        if nums[index] == key:
            target = nums[index + 1]
            follower_counts[target] += 1
            if follower_counts[target] > follower_counts[answer]:
                answer = target

    return answer
