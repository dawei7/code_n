def solve(tomatoSlices, cheeseSlices):
    extra_tomatoes = tomatoSlices - 2 * cheeseSlices
    if extra_tomatoes % 2 != 0:
        return []
    jumbo = extra_tomatoes // 2
    small = cheeseSlices - jumbo
    return [jumbo, small] if jumbo >= 0 and small >= 0 else []
