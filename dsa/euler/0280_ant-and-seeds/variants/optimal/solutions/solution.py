"""Project Euler 280: Ant and seeds

Find the expected number of steps for an ant starting at (2, 2) on a 5x5 grid
to carry all 5 seeds from the bottom row (r=0) to the top row (r=4).
"""

from __future__ import annotations


def solve() -> str:
    """Calculates the expected number of steps until all 5 seeds are transferred to the top row

    using backward dynamic programming over the 10 topological layers of the Markov decision process,
    solving exact 25x25 linear systems at each configuration via Gaussian elimination.
    """
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    adj: list[list[int]] = [[] for _ in range(25)]
    for r in range(5):
        for c in range(5):
            idx = r * 5 + c
            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 5 and 0 <= nc < 5:
                    adj[idx].append(nr * 5 + nc)

    def solve_linear_system(
        m_mat: list[list[float]], b_vec: list[float]
    ) -> list[float]:
        n = len(b_vec)
        augmented = [row[:] + [b_vec[i]] for i, row in enumerate(m_mat)]
        for i in range(n):
            pivot = i
            for r in range(i + 1, n):
                if abs(augmented[r][i]) > abs(augmented[pivot][i]):
                    pivot = r
            augmented[i], augmented[pivot] = augmented[pivot], augmented[i]

            piv = augmented[i][i]
            for c in range(i, n + 1):
                augmented[i][c] /= piv

            for r in range(n):
                if r != i:
                    factor = augmented[r][i]
                    for c in range(i, n + 1):
                        augmented[r][c] -= factor * augmented[i][c]

        return [augmented[i][n] for i in range(n)]

    # memo[(lower_mask, upper_mask, carrying)] -> list of 25 floats (expected remaining steps from each square)
    memo: dict[tuple[int, int, bool], list[float]] = {}
    memo[(0, 31, False)] = [0.0] * 25

    # Reverse topological layer processing: transferred seeds from 4 down to 0
    for transferred in range(4, -1, -1):
        for car in [True, False]:
            req_l = 5 - transferred - (1 if car else 0)
            req_u = transferred

            lmasks = [m for m in range(32) if bin(m).count("1") == req_l]
            umasks = [m for m in range(32) if bin(m).count("1") == req_u]

            for umask in umasks:
                for lmask in lmasks:
                    m_mat = [[0.0] * 25 for _ in range(25)]
                    b_vec = [1.0] * 25

                    for idx in range(25):
                        m_mat[idx][idx] = 1.0
                        deg = len(adj[idx])
                        prob = 1.0 / deg

                        for next_idx in adj[idx]:
                            nr = next_idx // 5
                            nc = next_idx % 5

                            next_lmask = lmask
                            next_umask = umask
                            next_car = car

                            if not car and nr == 0 and (next_lmask & (1 << nc)):
                                next_lmask &= ~(1 << nc)
                                next_car = True
                                e_dest = memo[(next_lmask, next_umask, next_car)][
                                    next_idx
                                ]
                                b_vec[idx] += prob * e_dest
                            elif (
                                car and nr == 4 and not (next_umask & (1 << nc))
                            ):
                                next_umask |= 1 << nc
                                next_car = False
                                e_dest = memo[(next_lmask, next_umask, next_car)][
                                    next_idx
                                ]
                                b_vec[idx] += prob * e_dest
                            else:
                                m_mat[idx][next_idx] -= prob

                    memo[(lmask, umask, car)] = solve_linear_system(
                        m_mat, b_vec
                    )

    start_expected = memo[(31, 0, False)][12]
    return f"{start_expected:.6f}"


if __name__ == "__main__":
    print(solve())
