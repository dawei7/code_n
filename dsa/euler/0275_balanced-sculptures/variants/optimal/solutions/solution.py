"""Project Euler 275: Balanced Sculptures

Find the number of balanced sculptures of order n = 18.
A sculpture is a polyomino of n blocks (y > 0) connected to a plinth at (0, 0),
with center of mass of blocks having x = 0 (sum(x) = 0), identifying reflections across y-axis.
"""

from __future__ import annotations


def solve(n: int = 18) -> str:
    """Calculates the number of balanced sculptures of order n using Redelmeier's polyomino

    enumeration algorithm on the upper half-plane with branch reachability bounding and
    depth-(n-1) exact coordinate targeting.
    """
    width = 40
    offset_x = 20

    def to_idx(x: int, y: int) -> int:
        return y * width + (x + offset_x)

    dx_dy = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    nbrs: list[list[int]] = [[] for _ in range(width * 25)]
    for y in range(1, 22):
        for x in range(-20, 21):
            idx = to_idx(x, y)
            for dx, dy in dx_dy:
                nx, ny = x + dx, y + dy
                if ny >= 1:
                    nbrs[idx].append(to_idx(nx, ny))

    root_idx = to_idx(0, 1)
    visited = [0] * (width * 25)
    in_poly = [0] * (width * 25)
    visited[root_idx] = 1
    in_poly[root_idx] = 1
    poly_cells = [0] * 25
    poly_cells[0] = root_idx

    cell_x = [(idx % width) - offset_x for idx in range(width * 25)]
    sym_idx_map = [to_idx(-cell_x[idx], idx // width) for idx in range(width * 25)]
    tri_rem = [r * (r + 1) // 2 for r in range(25)]

    sym_cnt = 0
    asym_cnt = 0

    def dfs(
        poly_len: int,
        sum_x: int,
        max_pos: int,
        min_neg: int,
        untried: list[int],
    ) -> None:
        nonlocal sym_cnt, asym_cnt

        # Leaf step optimization: at poly_len == n - 1, the last cell MUST have x == -sum_x
        if poly_len == n - 1:
            req_x = -sum_x
            for cell_idx in untried:
                if cell_x[cell_idx] == req_x:
                    poly_cells[n - 1] = cell_idx
                    in_poly[cell_idx] = 1

                    is_sym = True
                    for i in range(n):
                        if not in_poly[sym_idx_map[poly_cells[i]]]:
                            is_sym = False
                            break
                    if is_sym:
                        sym_cnt += 1
                    else:
                        asym_cnt += 1

                    in_poly[cell_idx] = 0
            return

        rem = n - poly_len
        if sum_x + rem * max_pos + tri_rem[rem] < 0:
            return
        if sum_x + rem * min_neg - tri_rem[rem] > 0:
            return

        while untried:
            cell_idx = untried.pop()
            x = cell_x[cell_idx]

            new_nbrs = [
                n_idx
                for n_idx in nbrs[cell_idx]
                if not visited[n_idx] and n_idx not in untried
            ]

            next_untried = list(untried)
            for n_idx in new_nbrs:
                next_untried.append(n_idx)
                visited[n_idx] = 1

            poly_cells[poly_len] = cell_idx
            in_poly[cell_idx] = 1
            dfs(
                poly_len + 1,
                sum_x + x,
                x if x > max_pos else max_pos,
                x if x < min_neg else min_neg,
                next_untried,
            )
            in_poly[cell_idx] = 0

            for n_idx in new_nbrs:
                visited[n_idx] = 0

    init_untried: list[int] = []
    for n_idx in nbrs[root_idx]:
        init_untried.append(n_idx)
        visited[n_idx] = 1

    dfs(1, 0, 0, 0, init_untried)
    total_sculptures = sym_cnt + asym_cnt // 2
    return str(total_sculptures)


if __name__ == "__main__":
    print(solve())
