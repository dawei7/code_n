def solve(s: str, t: str) -> bool:
    forward: dict[str, str] = {}
    reverse: dict[str, str] = {}
    for source, target in zip(s, t):
        if forward.get(source, target) != target or reverse.get(target, source) != source:
            return False
        forward[source] = target
        reverse[target] = source
    return True
