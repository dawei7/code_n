def solve(paths):
    starts = {path[0] for path in paths if len(path) >= 2}
    for path in paths:
        if len(path) >= 2 and path[1] not in starts:
            return path[1]
    return ""
