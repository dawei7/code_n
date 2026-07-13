def solve(flowerbed: list[int], n: int) -> bool:
    """Return whether the bed can fit at least n additional flowers."""
    if n == 0:
        return True

    planted = 0
    index = 0

    while index < len(flowerbed):
        left_empty = index == 0 or flowerbed[index - 1] == 0
        right_empty = (
            index == len(flowerbed) - 1
            or flowerbed[index + 1] == 0
        )

        if flowerbed[index] == 0 and left_empty and right_empty:
            planted += 1
            if planted >= n:
                return True
            index += 2
        else:
            index += 1

    return False

