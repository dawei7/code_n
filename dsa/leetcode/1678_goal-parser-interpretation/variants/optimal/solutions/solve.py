def solve(command: str) -> str:
    decoded: list[str] = []
    index = 0

    while index < len(command):
        if command[index] == "G":
            decoded.append("G")
            index += 1
        elif command[index + 1] == ")":
            decoded.append("o")
            index += 2
        else:
            decoded.append("al")
            index += 4

    return "".join(decoded)
