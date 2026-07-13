def solve(content: str, n: int) -> str:
    source_position = 0
    output: list[str] = []
    while len(output) < n:
        buffer = content[source_position : source_position + 4]
        source_position += len(buffer)
        if not buffer:
            break
        take = min(len(buffer), n - len(output))
        output.extend(buffer[:take])
        if len(buffer) < 4:
            break
    return "".join(output)
