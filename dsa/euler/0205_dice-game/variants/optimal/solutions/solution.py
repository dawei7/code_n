def solve() -> str:
    """Find probability that Pyramidal Peter beats Cubic Colin, rounded to 7 decimal places.
    
    Time Complexity: O(N_dice * faces)
    Space Complexity: O(max_sum)
    """
    peter = {0: 1}
    for _ in range(9):
        next_peter = {}
        for s, cnt in peter.items():
            for d in range(1, 5):
                next_peter[s + d] = next_peter.get(s + d, 0) + cnt
        peter = next_peter

    colin = {0: 1}
    for _ in range(6):
        next_colin = {}
        for s, cnt in colin.items():
            for d in range(1, 7):
                next_colin[s + d] = next_colin.get(s + d, 0) + cnt
        colin = next_colin

    total_peter = 4**9
    total_colin = 6**6

    win_ways = 0
    for s_p, cnt_p in peter.items():
        colin_less = sum(cnt_c for s_c, cnt_c in colin.items() if s_c < s_p)
        win_ways += cnt_p * colin_less

    prob = win_ways / (total_peter * total_colin)
    return f"{prob:.7f}"
