def solve(n: int) -> list[str]:
    result: list[str] = []
    path: list[str] = []

    def build(opened: int, closed: int) -> None:
        if len(path) == 2 * n:
            result.append("".join(path))
            return
        if opened < n:
            path.append("(")
            build(opened + 1, closed)
            path.pop()
        if closed < opened:
            path.append(")")
            build(opened, closed + 1)
            path.pop()

    build(0, 0)
    return result
