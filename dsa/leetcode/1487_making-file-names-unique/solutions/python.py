def solve(names):
    if not isinstance(names, list):
        names = [names]
    used = {}
    result = []
    for name in names:
        name = str(name)
        if name not in used:
            used[name] = 1
            result.append(name)
            continue
        suffix = used[name]
        while f"{name}({suffix})" in used:
            suffix += 1
        used[name] = suffix + 1
        unique = f"{name}({suffix})"
        used[unique] = 1
        result.append(unique)
    return result
