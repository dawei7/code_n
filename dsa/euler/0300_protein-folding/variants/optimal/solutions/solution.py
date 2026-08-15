"""Project Euler 300: Protein Folding

Find the average number of H-H contact points in an optimal 2D folding of a random protein string of length 15.
"""

from __future__ import annotations


def solve(n: int = 15) -> str:
    """Calculates the exact average number of H-H contacts over all 2^n protein strings of length n.

    1. Generate all self-avoiding walks (SAWs) of length n on Z^2 modulo rotations/reflections.
    2. Extract the non-consecutive contact graphs (pairs (i, j) with |i - j| > 1 and dist 1).
    3. Filter down to maximal contact graphs.
    4. For each of the 2^n protein strings, compute the maximum contacts over all foldings.
    5. Return the exact average as a decimal string.
    """
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    path: list[tuple[int, int]] = [(0, 0)] * n
    occupied: set[tuple[int, int]] = {(0, 0)}
    unique_graphs: set[frozenset[tuple[int, int]]] = set()

    def dfs(step: int) -> None:
        if step == n:
            edges: list[tuple[int, int]] = []
            for i in range(n):
                xi, yi = path[i]
                for j in range(i + 3, n, 2):
                    xj, yj = path[j]
                    if abs(xi - xj) + abs(yi - yj) == 1:
                        edges.append((i, j))
            if edges:
                unique_graphs.add(frozenset(edges))
            return

        px, py = path[step - 1]
        for dx, dy in dirs:
            nx, ny = px + dx, py + dy
            if (nx, ny) not in occupied:
                if step == 1 and (dx, dy) != (1, 0):
                    continue
                if step == 2 and (dx, dy) not in ((1, 0), (0, 1)):
                    continue
                occupied.add((nx, ny))
                path[step] = (nx, ny)
                dfs(step + 1)
                occupied.remove((nx, ny))

    dfs(1)

    # Filter to maximal graphs
    sorted_graphs = sorted(unique_graphs, key=len, reverse=True)
    maximal_graphs: list[frozenset[tuple[int, int]]] = []
    for g in sorted_graphs:
        if not any(g.issubset(mg) for mg in maximal_graphs):
            maximal_graphs.append(g)

    max_contacts = [0] * (1 << n)
    prepared_graphs = [[(1 << i) | (1 << j) for i, j in mg] for mg in maximal_graphs]

    for pair_masks in prepared_graphs:
        for m_val in range(1 << n):
            c = 0
            for pm in pair_masks:
                if (m_val & pm) == pm:
                    c += 1
            if c > max_contacts[m_val]:
                max_contacts[m_val] = c

    for m_val in range(1 << n):
        consec = sum(
            1 for i in range(n - 1) if (m_val & (1 << i)) and (m_val & (1 << (i + 1)))
        )
        max_contacts[m_val] += consec

    total_contacts = sum(max_contacts)
    avg = total_contacts / (1 << n)
    return str(avg)


if __name__ == "__main__":
    print(solve())
