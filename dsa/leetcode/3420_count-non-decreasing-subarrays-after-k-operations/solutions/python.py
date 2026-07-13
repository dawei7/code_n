from collections import deque


def solve(nums: list[int], k: int) -> int:
    n = len(nums)
    right = n - 1
    cost = 0
    answer = 0
    blocks = deque()

    for left in range(n - 1, -1, -1):
        while blocks and nums[left] > nums[blocks[-1]]:
            index = blocks.pop()
            next_index = blocks[-1] if blocks else right + 1
            cost += (next_index - index) * (nums[left] - nums[index])
        blocks.append(left)

        while cost > k:
            cost -= nums[blocks[0]] - nums[right]
            if blocks[0] == right:
                blocks.popleft()
            right -= 1

        answer += right - left + 1

    return answer
