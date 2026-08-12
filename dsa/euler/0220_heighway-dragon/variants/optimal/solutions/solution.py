DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def rotate_vec(x, y, d):
    if d == 0:
        return x, y
    if d == 1:
        return y, -x
    if d == 2:
        return -x, -y
    if d == 3:
        return -y, x


memo_a = {}
memo_b = {}


def get_full_a(k):
    if k in memo_a:
        return memo_a[k]
    if k == 0:
        return (0, 0, 0)
    dx1, dy1, r1 = get_full_a(k - 1)
    d1 = (0 + r1 + 1) % 4
    dx2, dy2, r2 = get_full_b(k - 1)
    dx2_rot, dy2_rot = rotate_vec(dx2, dy2, d1)
    d2 = (d1 + r2) % 4
    step_dx, step_dy = DIRS[d2]
    d_final = (d2 + 1) % 4

    total_dx = dx1 + dx2_rot + step_dx
    total_dy = dy1 + dy2_rot + step_dy
    net_rot = d_final
    memo_a[k] = (total_dx, total_dy, net_rot)
    return memo_a[k]


def get_full_b(k):
    if k in memo_b:
        return memo_b[k]
    if k == 0:
        return (0, 0, 0)
    d1 = 3
    step_dx, step_dy = DIRS[d1]
    dx1, dy1, r1 = get_full_a(k - 1)
    dx1_rot, dy1_rot = rotate_vec(dx1, dy1, d1)
    d2 = (d1 + r1 + 3) % 4
    dx2, dy2, r2 = get_full_b(k - 1)
    dx2_rot, dy2_rot = rotate_vec(dx2, dy2, d2)
    d_final = (d2 + r2) % 4

    total_dx = step_dx + dx1_rot + dx2_rot
    total_dy = step_dy + dy1_rot + dy2_rot
    net_rot = d_final
    memo_b[k] = (total_dx, total_dy, net_rot)
    return memo_b[k]


def sim_a(k, d, steps):
    if steps == 0 or k == 0:
        return (0, 0, d)
    max_s = (1 << k) - 1
    if steps >= max_s:
        full_dx, full_dy, r = get_full_a(k)
        rot_dx, rot_dy = rotate_vec(full_dx, full_dy, d)
        return (rot_dx, rot_dy, (d + r) % 4)

    max_prev = (1 << (k - 1)) - 1
    dx1, dy1, d1 = sim_a(k - 1, d, steps)
    rem = steps - max_prev
    if rem <= 0:
        return (dx1, dy1, d1)

    d2 = (d1 + 1) % 4
    dx2, dy2, d3 = sim_b(k - 1, d2, rem)
    rem -= max_prev
    if rem <= 0:
        return (dx1 + dx2, dy1 + dy2, d3)

    step_dx, step_dy = DIRS[d3]
    d4 = d3
    rem -= 1
    if rem <= 0:
        return (dx1 + dx2 + step_dx, dy1 + dy2 + step_dy, d4)

    d5 = (d4 + 1) % 4
    return (dx1 + dx2 + step_dx, dy1 + dy2 + step_dy, d5)


def sim_b(k, d, steps):
    if steps == 0 or k == 0:
        return (0, 0, d)
    max_s = (1 << k) - 1
    if steps >= max_s:
        full_dx, full_dy, r = get_full_b(k)
        rot_dx, rot_dy = rotate_vec(full_dx, full_dy, d)
        return (rot_dx, rot_dy, (d + r) % 4)

    d1 = (d + 3) % 4
    step_dx, step_dy = DIRS[d1]
    rem = steps - 1
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


def solve(order: int = 50, steps: int = 10**12) -> str:
    """Find position of cursor after `steps` steps in Heighway Dragon D_order.
    
    Time Complexity: O(order) via divide-and-conquer binary decomposition
    Space Complexity: O(order)
    """
    for k in range(order + 1):
        get_full_a(k)
        get_full_b(k)

    if steps == 0:
        return "0,0"

    dx, dy, _ = sim_a(order, 0, steps - 1)
    ans_x = 0 + dx
    ans_y = 1 + dy
    return f"{ans_x},{ans_y}"
