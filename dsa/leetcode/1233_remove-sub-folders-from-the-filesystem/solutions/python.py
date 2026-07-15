def solve(folder: list[str]) -> list[str]:
    folder.sort()
    result: list[str] = []
    for path in folder:
        if not result or not path.startswith(result[-1] + "/"):
            result.append(path)
    return result
