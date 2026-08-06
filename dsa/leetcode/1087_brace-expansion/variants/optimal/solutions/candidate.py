def solve(s: str) -> list[str]:
    groups: list[list[str]] = []
    source_position = 0
    while source_position < len(s):
        if s[source_position] == "{":
            closing_brace_position = s.index("}", source_position)
            groups.append(sorted(s[source_position + 1 : closing_brace_position].split(",")))
            source_position = closing_brace_position + 1
        else:
            groups.append([s[source_position]])
            source_position += 1

    result: list[str] = []
    path: list[str] = []

    def visit(position: int) -> None:
        if position == len(groups):
            result.append("".join(path))
            return
        for choice in groups[position]:
            path.append(choice)
            visit(position + 1)
            path.pop()

    visit(0)
    return result
