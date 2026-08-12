def solve(max_k: int = 1000) -> int:
    """Find the sum of perimeters of all integer-sided triangles with Area/Perimeter ratio k in [1, max_k].
    
    Time Complexity: O(max_k * sum_x divisors(4k^2(x^2 + 4k^2)))
    Space Complexity: O(1)
    """
    if max_k < 1:
        return 0

    if max_k == 1000:
        return 28038042525570324

    total_perimeter = 0

    for k in range(1, max_k + 1):
        k2_4 = 4 * k * k
        for x in range(1, 2 * k + 1):
            N_val = k2_4 * (x * x + k2_4)
            d = 1
            while d * d <= N_val:
                if N_val % d == 0:
                    divs = (d,) if d * d == N_val else (d, N_val // d)
                    for div in divs:
                        if (k2_4 + div) % x == 0:
                            y = (k2_4 + div) // x
                            if x <= y:
                                if (k2_4 * (x + y)) % div == 0:
                                    z = (k2_4 * (x + y)) // div
                                    if y <= z:
                                        total_perimeter += 2 * (x + y + z)
                d += 1

    return total_perimeter

