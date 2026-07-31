def solve(n: int) -> list[str]:
    valid: list[str] = []
    path: list[str] = []

    def generate() -> None:
        if len(path) == n:
            valid.append("".join(path))
            return

        path.append("1")
        generate()
        path.pop()

        if not path or path[-1] != "0":
            path.append("0")
            generate()
            path.pop()

    generate()
    return valid
