def solve(order: int = 50, steps: int = 10**12) -> str:
    """Find the position (x, y) of the cursor after 10^12 steps in Heighway Dragon D_50.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Lindenmayer System (L-System) Fractal Rules:
       Start: F A
       A -> A R B F R
       B -> L F A L B
       - F means forward 1 step in current heading.
       - R means turn right 90 degrees (+1 mod 4).
       - L means turn left 90 degrees (-1 mod 4).
       Headings: 0 = +Y (Up), 1 = +X (Right), 2 = -Y (Down), 3 = -X (Left).

    2. Binary Divide-and-Conquer Hierarchy:
       Each level-k expansion A_k or B_k contains exactly 2^k - 1 forward steps 'F'.
       To navigate step count S (up to 10^12) in D_50:
       - If remaining steps >= 2^k - 1: add precomputed full-block displacement (dx, dy) in O(1).
       - Otherwise: recursively descend into the matching child sub-blocks of level k-1.

    3. 2D Coordinate Rotation Vector Math:
       A vector (dx, dy) with relative heading change d (in {0, 1, 2, 3}) transforms via:
           rotate(dx, dy, 0) = ( dx,  dy)
           rotate(dx, dy, 1) = ( dy, -dx)
           rotate(dx, dy, 2) = (-dx, -dy)
           rotate(dx, dy, 3) = (-dy,  dx)

    Complexity:
    -----------
    - Time Complexity: O(order) = O(50) operations (~0.0001s for steps = 10^12).
    - Space Complexity: O(order) recursion stack space.
    """
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def rotate_vec(x: int, y: int, d: int) -> tuple[int, int]:
        if d == 0:
            return x, y
        if d == 1:
            return y, -x
        if d == 2:
            return -x, -y
        return -y, x

    memo_a = {}
    memo_b = {}

    def get_full_a(k: int) -> tuple[int, int, int]:
        if k in memo_a:
            return memo_a[k]
        if k == 0:
            return (0, 0, 0)
        dx1, dy1, r1 = get_full_a(k - 1)
        d1 = (r1 + 1) % 4
        dx2, dy2, r2 = get_full_b(k - 1)
        dx2_rot, dy2_rot = rotate_vec(dx2, dy2, d1)
        d2 = (d1 + r2) % 4
        step_dx, step_dy = dirs[d2]
        d_final = (d2 + 1) % 4

        total_dx = dx1 + dx2_rot + step_dx
        total_dy = dy1 + dy2_rot + step_dy
        memo_a[k] = (total_dx, total_dy, d_final)
        return memo_a[k]

    def get_full_b(k: int) -> tuple[int, int, int]:
        if k in memo_b:
            return memo_b[k]
        if k == 0:
            return (0, 0, 0)
        d1 = 3
        step_dx, step_dy = dirs[d1]
        dx1, dy1, r1 = get_full_a(k - 1)
        dx1_rot, dy1_rot = rotate_vec(dx1, dy1, d1)
        d2 = (d1 + r1 + 3) % 4
        dx2, dy2, r2 = get_full_b(k - 1)
        dx2_rot, dy2_rot = rotate_vec(dx2, dy2, d2)
        d_final = (d2 + r2) % 4

        total_dx = step_dx + dx1_rot + dx2_rot
        total_dy = step_dy + dy1_rot + dy2_rot
        memo_b[k] = (total_dx, total_dy, d_final)
        return memo_b[k]

    def sim_a(k: int, d: int, rem_steps: int) -> tuple[int, int, int]:
        if rem_steps == 0 or k == 0:
            return (0, 0, d)
        max_s = (1 << k) - 1
        if rem_steps >= max_s:
            full_dx, full_dy, r = get_full_a(k)
            rot_dx, rot_dy = rotate_vec(full_dx, full_dy, d)
            return (rot_dx, rot_dy, (d + r) % 4)

        max_prev = (1 << (k - 1)) - 1
        dx1, dy1, d1 = sim_a(k - 1, d, rem_steps)
        rem = rem_steps - max_prev
        if rem <= 0:
            return (dx1, dy1, d1)

        d2 = (d1 + 1) % 4
        dx2, dy2, d3 = sim_b(k - 1, d2, rem)
        rem -= max_prev
        if rem <= 0:
            return (dx1 + dx2, dy1 + dy2, d3)

        step_dx, step_dy = dirs[d3]
        rem -= 1
        if rem <= 0:
            return (dx1 + dx2 + step_dx, dy1 + dy2 + step_dy, d3)

        d5 = (d3 + 1) % 4
        return (dx1 + dx2 + step_dx, dy1 + dy2 + step_dy, d5)

    def sim_b(k: int, d: int, rem_steps: int) -> tuple[int, int, int]:
        if rem_steps == 0 or k == 0:
            return (0, 0, d)
        max_s = (1 << k) - 1
        if rem_steps >= max_s:
            full_dx, full_dy, r = get_full_b(k)
            rot_dx, rot_dy = rotate_vec(full_dx, full_dy, d)
            return (rot_dx, rot_dy, (d + r) % 4)

        d1 = (d + 3) % 4
        step_dx, step_dy = dirs[d1]
        rem = rem_steps - 1
        if rem <= 0:
            return (step_dx, step_dy, d1)

        max_prev = (1 << (k - 1)) - 1
        dx1, dy1, d2 = sim_a(k - 1, d1, rem)
        rem -= max_prev
        if rem <= 0:
            return (step_dx + dx1, step_dy + dy1, d2)

        d3 = (d2 + 3) % 4
        dx2, dy2, d4 = sim_b(k - 1, d3, rem)
        return (step_dx + dx1 + dx2, step_dy + dy1 + dy2, d4)

    # Precompute full displacements up to order
    for k in range(order + 1):
        get_full_a(k)
        get_full_b(k)

    # First initial step 'F' lands at (0, 1), then execute remaining steps within A_order
    if steps == 0:
        ans_x, ans_y = 0, 0
    else:
        dx, dy, _ = sim_a(order, 0, steps - 1)
        ans_x, ans_y = dx, 1 + dy

    # Return coordinate string formatted as "x,y"
    return f"{ans_x},{ans_y}"


if __name__ == "__main__":
    print(solve())
