import sys


MOD = 21945


def initial_counts(grid: list[bytes]) -> list[int]:
    seen = [[False] * 8 for _ in range(8)]
    counts = [0] * 16
    for sr in range(8):
        for sc in range(8):
            if grid[sr][sc] != 49 or seen[sr][sc]:
                continue
            stack = [(sr, sc)]
            seen[sr][sc] = True
            mask = 0
            while stack:
                r, c = stack.pop()
                if r == 0:
                    mask |= 1
                if r == 7:
                    mask |= 2
                if c == 0:
                    mask |= 4
                if c == 7:
                    mask |= 8
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < 8 and 0 <= nc < 8 and grid[nr][nc] == 49 and not seen[nr][nc]:
                        seen[nr][nc] = True
                        stack.append((nr, nc))
            counts[mask] += 1
    return counts


def transformed_masks(mask: int) -> list[int]:
    touches_top = bool(mask & 1)
    touches_bottom = bool(mask & 2)
    touches_left = bool(mask & 4)
    touches_right = bool(mask & 8)

    parent = list(range(4))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra = find(a)
        rb = find(b)
        if ra != rb:
            parent[rb] = ra

    # Copy ids: 0 = top-left, 1 = top-right, 2 = bottom-left, 3 = bottom-right.
    if touches_bottom:
        union(0, 2)
        union(1, 3)
    if touches_right:
        union(0, 1)
        union(2, 3)

    group_masks: dict[int, int] = {}
    for copy in range(4):
        top_half = copy < 2
        left_half = copy in (0, 2)
        new_mask = 0
        if touches_top:
            if top_half:
                new_mask |= 1
            else:
                new_mask |= 2
        if touches_left:
            if left_half:
                new_mask |= 4
            else:
                new_mask |= 8
        root = find(copy)
        group_masks[root] = group_masks.get(root, 0) | new_mask
    return list(group_masks.values())


def build_transform() -> list[list[int]]:
    matrix = [[0] * 16 for _ in range(16)]
    for old_mask in range(16):
        for new_mask in transformed_masks(old_mask):
            matrix[new_mask][old_mask] += 1
    return matrix


def mat_mul(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
    result = [[0] * 16 for _ in range(16)]
    for i in range(16):
        ri = result[i]
        for k in range(16):
            aik = a[i][k]
            if not aik:
                continue
            bk = b[k]
            for j in range(16):
                ri[j] = (ri[j] + aik * bk[j]) % MOD
    return result


def mat_vec_mul(matrix: list[list[int]], vector: list[int]) -> list[int]:
    return [sum(matrix[i][j] * vector[j] for j in range(16)) % MOD for i in range(16)]


TRANSFORM = build_transform()


def component_count_after_unfolds(counts: list[int], unfolds: int) -> int:
    matrix = TRANSFORM
    vector = [value % MOD for value in counts]
    while unfolds:
        if unfolds & 1:
            vector = mat_vec_mul(matrix, vector)
        unfolds >>= 1
        if unfolds:
            matrix = mat_mul(matrix, matrix)
    return sum(vector) % MOD


def main() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(tokens[idx])
        idx += 1
        grid = tokens[idx:idx + 8]
        idx += 8
        out.append(str(component_count_after_unfolds(initial_counts(grid), n - 3)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
