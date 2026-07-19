def solve(n: int, blacklist: list[int], draws: list[int]) -> list[int]:
    blocked = set(blacklist)
    bound = n - len(blacklist)
    remap: dict[int, int] = {}
    replacement = bound

    for value in blacklist:
        if value >= bound:
            continue
        while replacement in blocked:
            replacement += 1
        remap[value] = replacement
        replacement += 1

    return [remap.get(draw, draw) for draw in draws]
