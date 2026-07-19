def solve(s: str, p: str, removable: list[int]) -> int:
    removal_time = [len(removable)] * len(s)
    for time, index in enumerate(removable):
        removal_time[index] = time

    def remains_subsequence(removed_count: int) -> bool:
        pattern_index = 0
        for index, character in enumerate(s):
            if removal_time[index] >= removed_count and character == p[pattern_index]:
                pattern_index += 1
                if pattern_index == len(p):
                    return True
        return False

    low = 0
    high = len(removable)
    while low < high:
        middle = (low + high + 1) // 2
        if remains_subsequence(middle):
            low = middle
        else:
            high = middle - 1
    return low
