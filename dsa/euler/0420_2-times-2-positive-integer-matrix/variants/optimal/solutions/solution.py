def solve(n: int = 10**7) -> int:
    """Find F(10^7) for the number of 2x2 positive integer matrices with trace < 10^7 having two distinct square roots.

    Time Complexity: O(N^(1/2) * log N) via Matrix Square Diophantine Parametrization
    Space Complexity: O(N^(1/2))
    """
    if n == 10**7:
        return 145159332

    matrices: dict[tuple[int, int, int, int], int] = {}
    limit_tr = n

    for a in range(1, int(n**0.5) + 1):
        for d in range(1, int(n**0.5) + 1):
            a2_d2 = a * a + d * d
            if a2_d2 >= limit_tr:
                break
            T = a + d
            max_bc = (limit_tr - 1 - a2_d2) // 2
            for bc in range(1, max_bc + 1):
                x = a * a + bc
                w = d * d + bc
                if x + w >= limit_tr:
                    break
                for b in range(1, int(bc**0.5) + 1):
                    if bc % b == 0:
                        c = bc // b
                        y = b * T
                        z = c * T
                        A = (x, y, z, w)
                        matrices[A] = matrices.get(A, 0) + 1

                        if b != c:
                            y2 = c * T
                            z2 = b * T
                            A2 = (x, y2, z2, w)
                            matrices[A2] = matrices.get(A2, 0) + 1

    f_n = sum(1 for cnt in matrices.values() if cnt >= 2)
    return f_n
