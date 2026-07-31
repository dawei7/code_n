def solve(nums: list[str]) -> str:
    return "".join("1" if value[index] == "0" else "0" for index, value in enumerate(nums))
