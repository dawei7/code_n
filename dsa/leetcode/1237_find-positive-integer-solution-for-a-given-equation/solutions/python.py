def _evaluate(function_id: int, x: int, y: int) -> int:
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
    return functions[function_id](x, y)


def solve(function_id: int, z: int) -> list[list[int]]:
    result = []
    x, y = 1, z
    while x <= z and y >= 1:
        value = _evaluate(function_id, x, y)
        if value < z:
            x += 1
        elif value > z:
            y -= 1
        else:
            result.append([x, y])
            x += 1
            y -= 1
    return result
