def solve(groups: list[list[int]], nums: list[int]) -> bool:
    def find_end(pattern: list[int], start: int) -> int:
        prefix = [0] * len(pattern)
        matched = 0
        for index in range(1, len(pattern)):
            while matched and pattern[index] != pattern[matched]:
                matched = prefix[matched - 1]
            if pattern[index] == pattern[matched]:
                matched += 1
            prefix[index] = matched

        matched = 0
        for index in range(start, len(nums)):
            while matched and nums[index] != pattern[matched]:
                matched = prefix[matched - 1]
            if nums[index] == pattern[matched]:
                matched += 1
            if matched == len(pattern):
                return index + 1

        return -1

    position = 0
    for group in groups:
        position = find_end(group, position)
        if position == -1:
            return False

    return True
