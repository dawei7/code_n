def solve(reader: list[int], target: int) -> int:
    sentinel = 2**31 - 1

    def get(index: int) -> int:
        if index < len(reader):
            return reader[index]
        return sentinel

    left = 0
    right = 1

    while get(right) < target:
        left = right + 1
        right *= 2

    while left <= right:
        middle = (left + right) // 2
        value = get(middle)
        if value == target:
            return middle
        if value < target:
            left = middle + 1
        else:
            right = middle - 1

    return -1
