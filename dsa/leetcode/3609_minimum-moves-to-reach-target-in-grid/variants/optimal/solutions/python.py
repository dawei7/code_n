def solve(sx: int, sy: int, tx: int, ty: int) -> int:
    moves = 0

    while tx > sx or ty > sy:
        if tx < sx or ty < sy:
            return -1

        if tx == ty:
            if tx == 0:
                return -1
            if sy == 0:
                ty = 0
            elif sx == 0:
                tx = 0
            else:
                return -1
        elif tx > ty:
            if tx > 2 * ty:
                if tx % 2:
                    return -1
                tx //= 2
            else:
                tx -= ty
        else:
            if ty > 2 * tx:
                if ty % 2:
                    return -1
                ty //= 2
            else:
                ty -= tx

        moves += 1

    return moves if (tx, ty) == (sx, sy) else -1
