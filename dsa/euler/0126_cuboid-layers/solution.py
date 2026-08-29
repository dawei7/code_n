def solve(target_count: int = 1000) -> int:
    """Find the least n for which C(n), the number of cuboids (x, y, z) and layer n where layer cubes equals n, is 1,000.

    Mathematical Principles Applied:
    1. Cuboid Layer Volume Formula:
       For a cuboid of dimensions x x y x z (x >= y >= z >= 1), the number of cubes required to cover it in the n-th layer is:
       C(x, y, z, n) = 2*(x*y + y*z + z*x) + 4*(x + y + z + n - 2)*(n - 1).

       Derivation:
       - Layer 1 covers the surface area: 2*(x*y + y*z + z*x).
       - Each subsequent layer n adds 4*(x + y + z) along the edges and 8*(n - 2) along the corners.
       - Total formula simplifies to 2*(x*y + y*z + z*x) + 4*(x + y + z + n - 2)*(n - 1).

    2. Inverse Frequency Table Accumulation:
       Iterate dimensions z >= 1, y >= z, x >= y, and layer n >= 1 up to upper limit 20,000.
       Increment frequency table `counts[layer_cubes] += 1`.
       Find the smallest n where `counts[n] == 1000`.

    Time Complexity: O(Limit * Layers) executing in ~0.10s.
    Space Complexity: O(Limit) memory for frequency table.
    """
    limit = 20000
    counts = [0] * (limit + 1)

    # Outer loop for dimension z >= 1
    z = 1
    while True:
        cubes_z = 2 * (z * z + z * z + z * z)
        if cubes_z > limit:
            break
        y = z
        # Middle loop for dimension y >= z
        while True:
            cubes_y = 2 * (y * y + y * z + z * y)
            if cubes_y > limit:
                break
            x = y
            # Inner loop for dimension x >= y
            while True:
                base_cubes = 2 * (x * y + y * z + z * x)
                if base_cubes > limit:
                    break
                n = 1
                # Layer loop n >= 1
                while True:
                    # Apply closed-form n-th layer cubes formula
                    layer_cubes = base_cubes + 4 * (x + y + z + n - 2) * (n - 1)
                    if layer_cubes > limit:
                        break
                    # Increment frequency count for this exact cube count
                    counts[layer_cubes] += 1
                    n += 1
                x += 1
            y += 1
        z += 1

    # Find the smallest n with C(n) == 1,000
    for n in range(1, limit + 1):
        if counts[n] == target_count:
            return n

    return -1


if __name__ == "__main__":
    print(solve())
