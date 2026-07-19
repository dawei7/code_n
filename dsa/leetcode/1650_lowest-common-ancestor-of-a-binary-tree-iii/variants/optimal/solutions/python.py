def solve(p, q):
    first, second = p, q
    while first is not second:
        first = first.parent if first is not None else q
        second = second.parent if second is not None else p
    return first
