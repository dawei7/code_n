def solve(tomato_slices, cheese_slices):
    extra_tomatoes = tomato_slices - 2 * cheese_slices
    if extra_tomatoes % 2 != 0:
        return []
    jumbo = extra_tomatoes // 2
    small = cheese_slices - jumbo
    return [jumbo, small] if jumbo >= 0 and small >= 0 else []
