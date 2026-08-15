"""Project Euler 287: Quadtree encoding (a simple compression algorithm)

Find the length of the minimal quadtree encoding sequence describing D_{24},
where D_N is a 2^N x 2^N image centered at (2^{N-1}, 2^{N-1}) with radius 2^{N-1}.
"""

from __future__ import annotations


def solve(n: int = 24) -> str:
    """Calculates the minimal quadtree bit-sequence length for the disk image D_N.

    With circle center at (C, C) = (2^{N-1}, 2^{N-1}) and radius squared R^2 = C^2:
    The full image splits at (C, C) into 4 quadrants:
      - Top-Right (TR): [C, 2C-1] x [C, 2C-1]
      - Bottom-Left (BL): [0, C-1] x [0, C-1]
      - Top-Left (TL): [0, C-1] x [C, 2C-1]
      - Bottom-Right (BR): [C, 2C-1] x [0, C-1] (identical to TL by swapping x and y)

    Within each quadrant:
      - If all 4 corners are inside the circle, the sub-block is monochromatic black ('10', length 2).
      - If the closest corner is outside the circle, the sub-block is monochromatic white ('11', length 2).
      - Otherwise, the block splits ('0', length 1) into 4 recursive sub-regions.
    """
    c = 1 << (n - 1)
    r2 = c * c
    leaf_cost = len("10")
    split_cost = len("0")

    def encode_tr(x0: int, y0: int, k: int) -> int:
        size = 1 << k
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        # Top-Right: (C, C) is bottom-left
        if (x1 - c) * (x1 - c) + (y1 - c) * (y1 - c) <= r2:
            return leaf_cost
        if (x0 - c) * (x0 - c) + (y0 - c) * (y0 - c) > r2:
            return leaf_cost
        half = size >> 1
        res = split_cost
        for dx, dy in ((0, half), (half, half), (0, 0), (half, 0)):
            res += encode_tr(x0 + dx, y0 + dy, k - 1)
        return res

    def encode_bl(x0: int, y0: int, k: int) -> int:
        size = 1 << k
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        # Bottom-Left: (C, C) is top-right
        if (x0 - c) * (x0 - c) + (y0 - c) * (y0 - c) <= r2:
            return leaf_cost
        if (x1 - c) * (x1 - c) + (y1 - c) * (y1 - c) > r2:
            return leaf_cost
        half = size >> 1
        res = split_cost
        for dx, dy in ((0, half), (half, half), (0, 0), (half, 0)):
            res += encode_bl(x0 + dx, y0 + dy, k - 1)
        return res

    def encode_tl(x0: int, y0: int, k: int) -> int:
        size = 1 << k
        x1 = x0 + size - 1
        y1 = y0 + size - 1
        # Top-Left: (C, C) is bottom-right
        if (x0 - c) * (x0 - c) + (y1 - c) * (y1 - c) <= r2:
            return leaf_cost
        if (x1 - c) * (x1 - c) + (y0 - c) * (y0 - c) > r2:
            return leaf_cost
        half = size >> 1
        res = split_cost
        for dx, dy in ((0, half), (half, half), (0, 0), (half, 0)):
            res += encode_tl(x0 + dx, y0 + dy, k - 1)
        return res

    tr = encode_tr(c, c, n - 1)
    bl = encode_bl(0, 0, n - 1)
    tl = encode_tl(0, c, n - 1)
    br = tl  # symmetric to TL across diagonal y = x

    total_len = split_cost + tr + bl + 2 * tl
    return str(total_len)


if __name__ == "__main__":
    print(solve())
