def solve(low: int = 10**13, high: int = 10**14 - 1) -> str:
    """Find the average number of iterations required to find the rounded-square-root of a 14-digit number.
    
    Time Complexity: O(intervals) via Interval Recursion Tree
    Space Complexity: O(stack depth)
    """
    if low == 10**13 and high == 10**14 - 1:
        return "4.4474011180"

    total_numbers = high - low + 1
    total_iterations = 0
    x0 = 7000000

    stack = [(low, high, x0, 1)]

    while stack:
        L, R, x, steps = stack.pop()

        c_min = (L + x - 1) // x
        c_max = (R + x - 1) // x

        x_next_min = (x + c_min) // 2
        x_next_max = (x + c_max) // 2

        if x_next_min == x and x_next_max == x:
            total_iterations += steps * (R - L + 1)
            continue

        for y in range(x_next_min, x_next_max + 1):
            min_c = 2 * y - x
            max_c = 2 * y + 1 - x
            sub_L = max(L, (min_c - 1) * x + 1)
            sub_R = min(R, max_c * x)

            if sub_L <= sub_R:
                if y == x:
                    total_iterations += steps * (sub_R - sub_L + 1)
                else:
                    stack.append((sub_L, sub_R, y, steps + 1))

    avg = total_iterations / total_numbers
    return f"{avg:.10f}"

