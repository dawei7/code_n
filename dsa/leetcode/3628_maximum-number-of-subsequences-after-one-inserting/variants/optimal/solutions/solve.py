def solve(s: str) -> int:
    l_count = 0
    c_count = 0
    lc_count = 0
    ct_count = 0
    lct_count = 0
    total_t = s.count("T")

    for char in s:
        if char == "L":
            l_count += 1
        elif char == "C":
            c_count += 1
            lc_count += l_count
        elif char == "T":
            ct_count += c_count
            lct_count += lc_count

    best_c_gain = 0
    left_l = 0
    right_t = total_t
    for char in s:
        best_c_gain = max(best_c_gain, left_l * right_t)
        if char == "L":
            left_l += 1
        elif char == "T":
            right_t -= 1
    best_c_gain = max(best_c_gain, left_l * right_t)

    return lct_count + max(ct_count, lc_count, best_c_gain)
