def solve(n: int, rectangles: list[list[int]]) -> bool:
    def has_three_groups(start_index: int, end_index: int) -> bool:
        intervals = sorted((rectangle[start_index], rectangle[end_index]) for rectangle in rectangles)
        groups = 0
        current_end = -1

        for start, end in intervals:
            if start >= current_end:
                groups += 1
                if groups == 3:
                    return True
                current_end = end
            else:
                current_end = max(current_end, end)

        return False

    return has_three_groups(0, 2) or has_three_groups(1, 3)
