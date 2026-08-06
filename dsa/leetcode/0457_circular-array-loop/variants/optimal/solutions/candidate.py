"""Inert naming candidate for LeetCode 457."""


def solve(nums: list[int]) -> bool:
    length = len(nums)

    def advance(i: int, forward: bool) -> int:
        if nums[i] == 0 or (nums[i] > 0) != forward:
            return -1
        following = (i + nums[i]) % length
        if following == i:
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

        i = start
        while nums[i] != 0 and (nums[i] > 0) == forward:
            following = (i + nums[i]) % length
            nums[i] = 0
            i = following
    return False
