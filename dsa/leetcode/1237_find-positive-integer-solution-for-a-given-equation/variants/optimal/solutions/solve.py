class CustomFunction:
    """Local equivalent of LeetCode's hidden monotone-function interface."""

    def __init__(self, function_id: int):
        self.function_id = function_id

    def f(self, x: int, y: int) -> int:
        functions = (
            None,
            lambda a, b: a + b,
            lambda a, b: a * b,
            lambda a, b: a * a + b,
            lambda a, b: a + b * b,
            lambda a, b: a * a + b * b,
            lambda a, b: (a + b) * (a + b),
            lambda a, b: a * a * a + b * b * b,
            lambda a, b: a * a * b,
            lambda a, b: a * b * b,
        )
        return functions[self.function_id](x, y)


def solve(customfunction: CustomFunction, z: int) -> list[list[int]]:
    result = []
    x, y = 1, z
    while x <= z and y >= 1:
        value = customfunction.f(x, y)
        if value < z:
            x += 1
        elif value > z:
            y -= 1
        else:
            result.append([x, y])
            x += 1
            y -= 1
    return result
