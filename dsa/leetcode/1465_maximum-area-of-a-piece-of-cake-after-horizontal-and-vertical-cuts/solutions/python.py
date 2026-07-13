def solve(h, w, horizontal_cuts, vertical_cuts):
    mod = 1_000_000_007
    hs = [0, *sorted(cut for cut in horizontal_cuts if 0 < cut < h), h]
    vs = [0, *sorted(cut for cut in vertical_cuts if 0 < cut < w), w]
    max_h = max(hs[i + 1] - hs[i] for i in range(len(hs) - 1))
    max_w = max(vs[i + 1] - vs[i] for i in range(len(vs) - 1))
    return (max_h * max_w) % mod
