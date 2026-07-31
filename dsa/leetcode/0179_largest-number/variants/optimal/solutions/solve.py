from functools import cmp_to_key


def solve(nums: list[int]) -> str:
    def compare(left: str, right: str) -> int:
        if left + right > right + left:
            return -1
        if left + right < right + left:
            return 1
        return 0

    values = sorted((str(value) for value in nums), key=cmp_to_key(compare))
    if values[0] == "0":
        return "0"
    return "".join(values)
