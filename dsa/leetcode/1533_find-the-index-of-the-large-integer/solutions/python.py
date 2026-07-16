def solve(reader):
    left = 0
    right = reader.length() - 1

    while left < right:
        length = right - left + 1
        half = length // 2
        left_end = left + half - 1
        right_start = left + half
        right_end = right if length % 2 == 0 else right - 1
        comparison = reader.compareSub(left, left_end, right_start, right_end)
        if comparison > 0:
            right = left_end
        elif comparison < 0:
            left = right_start
            right = right_end
        else:
            return right
    return left
