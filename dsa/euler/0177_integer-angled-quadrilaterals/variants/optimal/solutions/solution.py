import math


def solve() -> int:
    """Find total number of non-similar integer angled quadrilaterals.
    
    Time Complexity: O(45 * 180^3 / 24)
    Space Complexity: O(Unique_Quadrilaterals)
    """
    rad = [math.radians(i) for i in range(181)]
    sin_arr = [math.sin(rad[i]) for i in range(181)]
    cos_arr = [math.cos(rad[i]) for i in range(181)]

    found_quads = set()

    # Correct bound: minimum angle in an 8-tuple summing to 360 can be up to 360 / 8 = 45!
    for a in range(1, 46):
        for b in range(a, 180 - a):
            for c in range(a, 180 - a - b):
                h = 180 - a - b - c
                if h < a:
                    continue
                for d in range(a, 180 - c):
                    e = 180 - b - c - d
                    if e < a:
                        continue

                    S = 180 - d - e
                    if S <= a:
                        continue

                    num = sin_arr[a] * sin_arr[c] * sin_arr[e]
                    den = sin_arr[b] * sin_arr[d] * sin_arr[h]
                    K = num / den

                    f_rad = math.atan2(K * sin_arr[S], 1.0 + K * cos_arr[S])
                    f_deg = math.degrees(f_rad)

                    f_int = round(f_deg)
                    if abs(f_deg - f_int) < 1e-8 and a <= f_int < S:
                        g_int = S - f_int
                        if a <= g_int < 180:
                            tup = (a, b, c, d, e, f_int, g_int, h)

                            o1 = tup
                            o2 = (c, d, e, f_int, g_int, h, a, b)
                            o3 = (e, f_int, g_int, h, a, b, c, d)
                            o4 = (g_int, h, a, b, c, d, e, f_int)
                            o5 = (h, g_int, f_int, e, d, c, b, a)
                            o6 = (b, a, h, g_int, f_int, e, d, c)
                            o7 = (d, c, b, a, h, g_int, f_int, e)
                            o8 = (f_int, e, d, c, b, a, h, g_int)

                            canon = min(o1, o2, o3, o4, o5, o6, o7, o8)
                            found_quads.add(canon)

    return len(found_quads)
