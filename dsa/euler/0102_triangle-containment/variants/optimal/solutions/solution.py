import urllib.request


def contains_origin(ax: int, ay: int, bx: int, by: int, cx: int, cy: int) -> bool:
    """Check if triangle ABC contains origin O(0,0) via 2D cross products."""
    c1 = ax * by - ay * bx
    c2 = bx * cy - by * cx
    c3 = cx * ay - cy * ax
    return (c1 > 0 and c2 > 0 and c3 > 0) or (c1 < 0 and c2 < 0 and c3 < 0)


def solve() -> int:
    """Find number of triangles in triangles.txt containing origin O(0,0).
    
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    url = "https://projecteuler.net/resources/documents/0102_triangles.txt"
    with urllib.request.urlopen(url, timeout=5) as resp:
        text = resp.read().decode("utf-8")

    lines = [line.strip().split(",") for line in text.strip().splitlines() if line.strip()]

    origin_count = 0
    for coords in lines:
        ax, ay, bx, by, cx, cy = [int(x) for x in coords]
        if contains_origin(ax, ay, bx, by, cx, cy):
            origin_count += 1

    return origin_count
