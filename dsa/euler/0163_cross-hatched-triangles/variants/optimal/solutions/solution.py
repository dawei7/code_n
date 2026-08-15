def solve(n: int = 36) -> int:
    """Count all triangles in a cross-hatched equilateral triangle of size n.

    A cross-hatched equilateral triangle of side n has medians drawn inside every
    unit triangle, producing 6 families of lines in the (X, Y) coordinate system
    where vertices are (0,0), (2n,0), (n,n):
      3 edge-parallel: Y=const, X-Y=const, X+Y=const
      3 median-parallel: X-3Y=const, X+3Y=const, X=const
    A triangle is formed by any 3 lines from 3 distinct families whose pairwise
    intersections all lie inside the big triangle.  Coordinates are scaled by 12
    to keep exact integer arithmetic (LCM of all pairwise determinants).

    Time Complexity: O(n^3)
    Space Complexity: O(n)
    """
    # Line families: aX + bY = value
    fa = [(0, 1), (1, -1), (1, 1), (1, -3), (1, 3), (1, 0)]

    # Valid line values for each family
    fv = [
        list(range(n + 1)),
        [2 * k for k in range(n + 1)],
        [2 * k for k in range(n + 1)],
        [2 * m for m in range(-(n - 1), n)],
        [2 * m for m in range(1, 2 * n)],
        list(range(1, 2 * n)),
    ]

    bound = 24 * n  # 12-scaled upper bound: 12*(X+Y) <= 12*2n
    total = 0

    for fi in range(6):
        ai, bi = fa[fi]
        for fj in range(fi + 1, 6):
            aj, bj = fa[fj]
            dij = ai * bj - aj * bi
            if dij == 0:
                continue
            for fk in range(fj + 1, 6):
                ak, bk = fa[fk]
                dik = ai * bk - ak * bi
                djk = aj * bk - ak * bj
                if dik == 0 or djk == 0:
                    continue

                for ci in fv[fi]:
                    for cj in fv[fj]:
                        # Intersection of lines fi and fj, in 12-scaled coords
                        Xij = 12 * (ci * bj - cj * bi) // dij
                        Yij = 12 * (ai * cj - aj * ci) // dij
                        if Yij < 0 or Xij < Yij or Xij + Yij > bound:
                            continue

                        for ck in fv[fk]:
                            # Intersection of fi and fk
                            Xik = 12 * (ci * bk - ck * bi) // dik
                            Yik = 12 * (ai * ck - ak * ci) // dik
                            if Yik < 0 or Xik < Yik or Xik + Yik > bound:
                                continue

                            # Intersection of fj and fk
                            Xjk = 12 * (cj * bk - ck * bj) // djk
                            Yjk = 12 * (aj * ck - ak * cj) // djk
                            if Yjk < 0 or Xjk < Yjk or Xjk + Yjk > bound:
                                continue

                            # Non-degeneracy: three distinct points
                            if (Xij == Xik and Yij == Yik) or \
                               (Xij == Xjk and Yij == Yjk) or \
                               (Xik == Xjk and Yik == Yjk):
                                continue

                            total += 1

    return total


if __name__ == "__main__":
    print(solve())
