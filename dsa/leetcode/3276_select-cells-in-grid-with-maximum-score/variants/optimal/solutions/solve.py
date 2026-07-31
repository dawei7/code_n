from functools import lru_cache


def solve(grid: list[list[int]]) -> int:
    rows_by_value: dict[int, list[int]] = {}

    for row_index, row in enumerate(grid):
        for value in set(row):
            rows_by_value.setdefault(value, []).append(row_index)

    values = list(rows_by_value)

    @lru_cache(None)
    def search(value_index: int, used_rows: int) -> int:
        if value_index == len(values):
            return 0

        value = values[value_index]
        answer = search(value_index + 1, used_rows)

        for row_index in rows_by_value[value]:
            row_bit = 1 << row_index
            if used_rows & row_bit == 0:
                answer = max(
                    answer,
                    value + search(value_index + 1, used_rows | row_bit),
                )

        return answer

    return search(0, 0)
