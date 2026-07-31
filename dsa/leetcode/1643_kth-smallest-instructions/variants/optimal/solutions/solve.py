from math import comb


def solve(destination: list[int], k: int) -> str:
    vertical, horizontal = destination
    instructions: list[str] = []

    while horizontal and vertical:
        starting_with_horizontal = comb(horizontal + vertical - 1, vertical)
        if k <= starting_with_horizontal:
            instructions.append("H")
            horizontal -= 1
        else:
            instructions.append("V")
            vertical -= 1
            k -= starting_with_horizontal

    instructions.extend("H" * horizontal)
    instructions.extend("V" * vertical)
    return "".join(instructions)
