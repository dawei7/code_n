"""Boundary binary searches for LeetCode 302."""


def _minimum_area(image, x: int, y: int) -> int:
    rows = len(image)
    columns = len(image[0])

    def search_columns(left: int, right: int, seek_black: bool) -> int:
        while left < right:
            middle = (left + right) // 2
            has_black = any(image[row][middle] == "1" for row in range(rows))
            if has_black == seek_black:
                right = middle
            else:
                left = middle + 1
        return left

    def search_rows(top: int, bottom: int, seek_black: bool) -> int:
        while top < bottom:
            middle = (top + bottom) // 2
            has_black = any(image[middle][column] == "1" for column in range(columns))
            if has_black == seek_black:
                bottom = middle
            else:
                top = middle + 1
        return top

    left = search_columns(0, y, True)
    right = search_columns(y + 1, columns, False)
    top = search_rows(0, x, True)
    bottom = search_rows(x + 1, rows, False)
    return (right - left) * (bottom - top)


def solve(image: list[str], x: int, y: int) -> int:
    return _minimum_area(image, x, y)
