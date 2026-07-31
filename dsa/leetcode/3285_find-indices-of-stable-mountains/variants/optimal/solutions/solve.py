def solve(height: list[int], threshold: int) -> list[int]:
    return [index for index in range(1, len(height)) if height[index - 1] > threshold]
