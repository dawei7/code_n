from collections import deque


class Solution:
    def minOperations(self, grid: list[list[int]], k: int) -> int:
        rows = len(grid)
        columns = len(grid[0])
        start_columns = columns - k + 1

        base_columns = [0] * start_columns
        coefficient_columns = [0] * start_columns
        recent_rows = deque()

        lower_bound = max(max(row) for row in grid)
        upper_bound = None
        forced_target = None
        base_total = 0
        coefficient_total = 0

        def require_nonnegative(coefficient: int, base: int) -> bool:
            nonlocal lower_bound, upper_bound

            if coefficient > 0:
                lower_bound = max(lower_bound, -(base // coefficient))
            elif coefficient < 0:
                bound = (-base) // coefficient
                upper_bound = bound if upper_bound is None else min(upper_bound, bound)
            elif base < 0:
                return False

            return True

        def require_zero(coefficient: int, base: int) -> bool:
            nonlocal forced_target

            if coefficient == 0:
                return base == 0
            if (-base) % coefficient != 0:
                return False

            target = (-base) // coefficient
            if forced_target is not None and forced_target != target:
                return False
            forced_target = target
            return True

        for row in range(rows):
            if len(recent_rows) == k:
                expired_bases, expired_coefficients = recent_rows.popleft()
                for column in range(start_columns):
                    base_columns[column] -= expired_bases[column]
                    coefficient_columns[column] -= expired_coefficients[column]

            row_bases = [0] * start_columns
            row_coefficients = [0] * start_columns
            base_window = 0
            coefficient_window = 0

            for column in range(columns):
                if column < start_columns:
                    base_window += base_columns[column]
                    coefficient_window += coefficient_columns[column]

                expired_column = column - k
                if 0 <= expired_column < start_columns:
                    base_window -= base_columns[expired_column]
                    coefficient_window -= coefficient_columns[expired_column]

                current_base = grid[row][column] + base_window
                current_coefficient = coefficient_window

                if row + k <= rows and column + k <= columns:
                    operation_base = -current_base
                    operation_coefficient = 1 - current_coefficient

                    if not require_nonnegative(
                        operation_coefficient, operation_base
                    ):
                        return -1

                    row_bases[column] = operation_base
                    row_coefficients[column] = operation_coefficient
                    base_columns[column] += operation_base
                    coefficient_columns[column] += operation_coefficient
                    base_window += operation_base
                    coefficient_window += operation_coefficient
                    base_total += operation_base
                    coefficient_total += operation_coefficient
                elif not require_zero(
                    current_coefficient - 1, current_base
                ):
                    return -1

            recent_rows.append((row_bases, row_coefficients))

        target = lower_bound if forced_target is None else forced_target
        if target < lower_bound:
            return -1
        if upper_bound is not None and target > upper_bound:
            return -1

        return coefficient_total * target + base_total
