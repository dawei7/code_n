"""Project Euler 260: Stone Game

Find the sum of (x_i + y_i + z_i) over all losing configurations (x_i, y_i, z_i)
with x_i <= y_i <= z_i <= 1000 in the 3-pile Nim/Wythoff game.
"""

from __future__ import annotations


def solve(limit: int = 1000) -> str:
    """Computes the sum of all losing positions (x, y, z) with x <= y <= z <= limit

    using 3D state marking across all 7 legal move directions.
    """
    n = limit + 1
    n2 = n * n
    is_winning = bytearray(n * n2)

    total_sum = 0

    for x in range(n):
        x_n2 = x * n2
        for y in range(x, n):
            xy = x_n2 + y * n
            for z in range(y, n):
                if not is_winning[xy + z]:
                    total_sum += x + y + z

                    # 1-pile moves (along 3 axes)
                    for k in range(1, n - z):
                        is_winning[xy + (z + k)] = 1
                    for k in range(1, n - y):
                        yk = y + k
                        if yk <= z:
                            is_winning[x_n2 + yk * n + z] = 1
                        else:
                            is_winning[x_n2 + z * n + yk] = 1
                    for k in range(1, n - x):
                        xk = x + k
                        if xk <= y:
                            is_winning[xk * n2 + y * n + z] = 1
                        elif xk <= z:
                            is_winning[y * n2 + xk * n + z] = 1
                        else:
                            is_winning[y * n2 + z * n + xk] = 1

                    # 2-pile moves (along 3 diagonal planes)
                    for k in range(1, min(n - x, n - y)):
                        xk = x + k
                        yk = y + k
                        if yk <= z:
                            is_winning[xk * n2 + yk * n + z] = 1
                        elif xk <= z:
                            is_winning[xk * n2 + z * n + yk] = 1
                        else:
                            is_winning[z * n2 + xk * n + yk] = 1
                    for k in range(1, min(n - x, n - z)):
                        xk = x + k
                        zk = z + k
                        if xk <= y:
                            is_winning[xk * n2 + y * n + zk] = 1
                        else:
                            is_winning[y * n2 + xk * n + zk] = 1
                    for k in range(1, min(n - y, n - z)):
                        yk = y + k
                        zk = z + k
                        is_winning[x_n2 + yk * n + zk] = 1

                    # 3-pile moves (along main diagonal ray)
                    for k in range(1, min(n - x, n - y, n - z)):
                        is_winning[(x + k) * n2 + (y + k) * n + (z + k)] = 1

                    # For a fixed (x, y), there is at most one losing z, so break
                    break

    return str(total_sum)


if __name__ == "__main__":
    print(solve())
