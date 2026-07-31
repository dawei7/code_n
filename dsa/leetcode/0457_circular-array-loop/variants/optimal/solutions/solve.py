"""In-place Floyd-cycle solution for LeetCode 457."""


def solve(nums: list[int]) -> bool:
    length = len(nums)

    def advance(index: int, forward: bool) -> int:
        if nums[index] == 0 or (nums[index] > 0) != forward:
            return -1
        following = (index + nums[index]) % length
        if following == index:
            return -1
        return following

    for start in range(length):
        if nums[start] == 0:
            continue
        forward = nums[start] > 0
        slow = fast = start
        while True:
            slow = advance(slow, forward)
            if slow == -1:
                break
            fast = advance(fast, forward)
            if fast == -1:
                break
            fast = advance(fast, forward)
            if fast == -1:
                break
            if slow == fast:
                return True

        index = start
        while nums[index] != 0 and (nums[index] > 0) == forward:
            following = (index + nums[index]) % length
            nums[index] = 0
            index = following
    return False
