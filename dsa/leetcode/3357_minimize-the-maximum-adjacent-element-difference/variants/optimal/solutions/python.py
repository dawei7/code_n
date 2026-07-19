def solve(nums: list[int]) -> int:
    max_fixed_gap = 0
    min_boundary = 10**9
    max_boundary = 0

    for left, right in zip(nums, nums[1:]):
        if (left == -1) != (right == -1):
            value = max(left, right)
            min_boundary = min(min_boundary, value)
            max_boundary = max(max_boundary, value)
        elif left != -1:
            max_fixed_gap = max(max_fixed_gap, abs(left - right))

    if max_boundary == 0:
        return max_fixed_gap

    def check_single_gap(a: int, b: int, limit: int, x: int, y: int) -> bool:
        return min(max(abs(a - x), abs(b - x)), max(abs(a - y), abs(b - y))) <= limit

    def check_multiple_gap(a: int, b: int, limit: int, x: int, y: int) -> bool:
        ax = abs(a - x)
        ay = abs(a - y)
        bx = abs(b - x)
        by = abs(b - y)
        xy = abs(x - y)
        return min(max(ax, bx), max(ay, by), max(ax, xy, by), max(ay, xy, bx)) <= limit

    def check_boundary_gap(value: int, limit: int, x: int, y: int) -> bool:
        return min(abs(value - x), abs(value - y)) <= limit

    def feasible(limit: int) -> bool:
        x = min_boundary + limit
        y = max_boundary - limit
        gap_length = 0
        previous = 0

        for value in nums:
            if value == -1:
                gap_length += 1
                continue
            if previous > 0 and gap_length > 0:
                if gap_length == 1 and not check_single_gap(previous, value, limit, x, y):
                    return False
                if gap_length > 1 and not check_multiple_gap(previous, value, limit, x, y):
                    return False
            previous = value
            gap_length = 0

        if nums[0] == -1:
            first = next((value for value in nums if value != -1), -1)
            if first != -1 and not check_boundary_gap(first, limit, x, y):
                return False

        if nums[-1] == -1:
            last = next((value for value in reversed(nums) if value != -1), -1)
            if last != -1 and not check_boundary_gap(last, limit, x, y):
                return False

        return True

    low = max_fixed_gap
    high = max(low, (max_boundary - min_boundary + 1) // 2)
    while low < high:
        mid = (low + high) // 2
        if feasible(mid):
            high = mid
        else:
            low = mid + 1

    return low
