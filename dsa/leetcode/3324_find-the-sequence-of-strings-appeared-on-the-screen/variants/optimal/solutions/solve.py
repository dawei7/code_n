def solve(target: str) -> list[str]:
    screen = []
    sequence = []

    for desired in target:
        screen.append("a")
        sequence.append("".join(screen))

        while screen[-1] != desired:
            screen[-1] = chr(ord(screen[-1]) + 1)
            sequence.append("".join(screen))

    return sequence
