def solve(sx: int, sy: int, tx: int, ty: int) -> bool:
    while tx > sx and ty > sy:
        if tx > ty:
            tx %= ty
        else:
            ty %= tx

    if tx == sx:
        return ty >= sy and (ty - sy) % sx == 0
    if ty == sy:
        return tx >= sx and (tx - sx) % sy == 0
    return False
