def solve(n: int, blacklist: list[int], draws: list[int]) -> list[int]:
    blocked = set(blacklist)
    bound = n - len(blacklist)
    remap = {}
    replacement = bound

    for value in blacklist:
        if value >= bound:
            continue
        while replacement in blocked:
            replacement += 1
        remap[value] = replacement
        replacement += 1

    position = 0

    def randrange(stop: int) -> int:
        nonlocal position
        draw = draws[position]
        position += 1
        if not 0 <= draw < stop:
            raise ValueError("each deterministic draw must be in [0, bound)")
        return draw

    def pick() -> int:
        draw = randrange(bound)
        return remap.get(draw, draw)

    return [pick() for _ in draws]
