def solve(target_count: int = 1000) -> int:
    """Find least n for which C(n) = target_count using cuboid layer expansion formula.
    
    Time Complexity: O(N_max * LayerCount)
    Space Complexity: O(N_max)
    """
    limit = 20000
    counts = [0] * (limit + 1)

    # 2*(x*y + y*z + z*x) + 4*(x + y + z + n - 2)*(n - 1)
    z = 1
    while True:
        cubes_z = 2 * (z * z + z * z + z * z)
        if cubes_z > limit:
            break
        y = z
        while True:
            cubes_y = 2 * (y * y + y * z + z * y)
            if cubes_y > limit:
                break
            x = y
            while True:
                base_cubes = 2 * (x * y + y * z + z * x)
                if base_cubes > limit:
                    break
                n = 1
                while True:
                    layer_cubes = base_cubes + 4 * (x + y + z + n - 2) * (n - 1)
                    if layer_cubes > limit:
                        break
                    counts[layer_cubes] += 1
                    n += 1
                x += 1
            y += 1
        z += 1

    for n in range(1, limit + 1):
        if counts[n] == target_count:
            return n

    return -1
